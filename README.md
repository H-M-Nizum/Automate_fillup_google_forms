# Automate Google Forms Fill-Up
This Python project automates the process of filling out Google Forms using web automation. It is designed to streamline repetitive form submission tasks by filling in the required fields programmatically.

## Features
    - Automatically fill out Google Forms with predefined responses
    - Handle multiple types of input fields (text, multiple choice, checkboxes, etc.)
    - Supports submitting multiple forms in one go
    - Configurable via Python scripts and JSON/CSV for inputs
    - Customizable to match the specific Google Form layout
## Technologies Used
    1. Python: The core language used for scripting the automation.
    2. Selenium: For web automation, interacting with the Google Forms through a web browser.
    3. WebDriver: Required for controlling the browser (Chrome, Firefox, etc.)
    4. Pandas: Employed for handling and manipulating input data, especially when working with large datasets in CSV or other tabular formats.
    5. Faker: Used to generate fake data for testing purposes, such as random names, emails, and other form fields.
## Prerequisites
Python 3.x: Make sure you have Python installed on your system.
Selenium: Install the library using:
  ``
    pip install selenium
    pip install pandas
    pip install Faker
  ``
WebDriver: Download the appropriate WebDriver for your browser and ensure it is in your system PATH.
## Installation
  1. Clone the repository to your local machine:
  ``
    git clone https://github.com/H-M-Nizum/Automate_fillup_google_forms.git
    cd Automate_fillup_google_forms
  ``
  2. Install the required Python dependencies:
  ``
    pip install -r requirements.txt
  ``
  3. Set up your WebDriver (ChromeDriver, GeckoDriver, etc.) and ensure it is executable.

## Usage
  1. Run the script to start the automation:
   ``
    python automate_fill.py
  ``
  2. The script will launch a browser, navigate to the Google Form, fill in the responses, and submit the form.


## Contact
For any questions or issues, please feel free to contact me at your email.
``
hmnizum1714032@gmail.com
``
