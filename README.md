-> Python Assignment Submission: Google Form Automation and Automated Email :

This repository contains the complete solution for the assignment, demonstrating skills in web automation (Selenium) and backend process automation (Flask/Flask-Mail).

->Project Components :

The solution is divided into two primary parts:

Form Filler (form_filler.py): A Python script using Selenium to automatically fill out the specified Google Form.

Email Sender (app.py): A lightweight Flask application used to send the final submission email programmatically, as required by the assignment.

-> Prerequisites: 

To run this project, you need:

Python 3.x

Google Chrome installed.

The corresponding ChromeDriver executable configured in your system's PATH.

A Gmail App Password if you use Gmail for submission (required for SMTP security).

Installation

Install the necessary Python dependencies using the requirements.txt file:

pip install -r requirements.txt


-> Technical Approach :

1. Google Form Filling (form_filler.py)

The script is engineered for robustness against common Google Forms HTML structures:

Field Group

Data Variables

Locator Strategy

Rationale

Short/Long Text (Name, Contact, Email, Address, Pin Code, Gender, CAPTCHA)

TEXT_INPUT_DATA

driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], textarea')

Uses a single selector for sequential iteration, targeting generic text inputs without relying on unstable class names.

Date Input (Date of Birth)

DOB_DATA

//input[@type='date']

Targets the field by its unique HTML type attribute, ensuring precision.

Submission

N/A

//span[text()='Submit']/ancestor::div[@role='button']

A highly stable XPath that finds the submit button based on the visible 'Submit' text.

Key Feature: The script includes driver.execute_script("arguments[0].scrollIntoView(true);", element) before interacting with each field to ensure the element is visible, preventing potential ElementNotInteractableException errors across different screen resolutions.

2. Automated Email Submission (app.py)

The email requirement is met using the Flask framework and the Flask-Mail extension.

Configuration (config.py): All sensitive SMTP credentials and recipient emails are isolated in config.py. This file must be updated by the user.

Submission Route: A simple route /submit is used to trigger the email sending process.

Content Generation: The email body is programmatically constructed in app.py to confirm all 6 submission requirements (including the confirmation of full-time availability and the links to the repository and projects).

Usage Instructions : 

Step 1: Configuration

Update config.py: Fill in your personal MAIL_USERNAME, MAIL_PASSWORD, and set the GITHUB_REPO_URL to your repository link.

Update CAPTCHA: Due to the dynamic nature of CAPTCHAs, you must manually inspect the form and update the corresponding value in the TEXT_INPUT_DATA dictionary in form_filler.py (index 6) before execution.

Step 2: Run Form Filler

Run the Selenium script to fill the form and capture the required screenshot.

python form_filler.py


The script will launch Chrome, fill the data, and click the Submit button (ensure this line is uncommented).

A 10-second pause is included after submission to give you time to capture the required Screenshot (Requirement #1) of the successful submission page.

Step 3: Send Submission Email

Run the Flask application:

python app.py


Send Email: Navigate to the submission route in your browser (e.g., http://127.0.0.1:5000/submit). The email will be sent immediately upon visiting this page.


