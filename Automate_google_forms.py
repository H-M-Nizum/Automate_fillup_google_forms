from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from faker import Faker



# Set up the WebDriver 
driver_path = 'E:/Dowmnload/Driver/chromedriver.exe' 
service = Service(driver_path)  # Create a Service object
driver = webdriver.Chrome(service=service)  # Initialize the WebDriver using the Service object

# Load the website
url = 'https://forms.gle/nEwpCecztfydkwCo6'
# Wait 5 second for wesite load

while True:
    response = int(input('Enter Number Of Responses : '))
    
    # Generating fake data
    fake = Faker()
    profile = [fake.profile() for i in range(response)]  	# create a fake data list for  personal info
    df = pd.DataFrame(profile)   # Create pandas DataFrame
    df = df[['name', 'mail', 'address']] # Take only three columns
    phone = [fake.phone_number() for i in range(response)] # Create fake phone number list
    df['Phone number'] = phone # Add the list in DataFrame
    comment = [fake.paragraph(nb_sentences=1) for i in range(response)] # Create fake one sentence paragraph for comment
    df['Comments'] = comment # Add the list in DataFrame
    df.rename(columns={'name':'Name', 'mail':'Email', 'address':'Address'}, inplace=True) # Change the columns name
        
    # Iterating over rows and columns properly
    for row in df.index:  # Iterating over the row indices
        driver.get(url) # Load the website
        time.sleep(1) 
        for col in df.columns:  # Iterating over the column names
            # Call dynamic XPATH for input/textarea
            name = driver.find_element(By.XPATH, f"//div[contains(@data-params, '{col}')]//input | //div[contains(@data-params, '{col}')]//textarea")
            name.send_keys(df.loc[row, col]) # fill the form field
            time.sleep(1)
        submit = driver.find_element(By.XPATH, "//div[@role='button']//span[text()='জমা দিন'] | //div[@role='button']//span[text()='Submit']")
        submit.click() # Click submit button

    print(f"""Press 1 : If You Want Submit Another Responses Series.
    Press 2 : If you Want Stop This Process.""")
    exit = int(input("Enter A Number : "))
    if exit == 2:
        break