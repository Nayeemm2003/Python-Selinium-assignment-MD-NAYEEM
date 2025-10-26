import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuration 
FORM_URL = "https://forms.gle/WT68aV5UnPajeoSc8"

# (Full Name, Contact, Email, Address, Pin, Gender, CAPTCHA)
TEXT_INPUT_DATA = {
    0: "MD NAYEEM",                                  # Full Name (Text Input 0)
    1: "8368888969",                                 # Contact Number (Text Input 1)
    2: "mohdnayeemm2003@gmail.com",                  # Email ID (Text Input 2)
    3: "D-45 MADANPUR KHADAR EXTN-3 NEAR MAKKI MASJID NEW DELHI", # Full Address (Text Input 3)
    4: "110076",                                     # Pin Code (Text Input 4)
    5: "MALE",                                       # Gender (Text Input 5)
    6: "GNFPYC"                                      # CAPTCHA code (Text Input 6)
}

# Data for Date of Birth field in DD/MM/YYYY format
DOB_DATA = "29/10/2003"

# No radio button data needed, as Gender is a text field.
RADIO_CHOICE_DATA = {}
CHECKBOX_CHOICE_DATA = {}

def fill_google_form():
    
    print("Starting WebDriver...")

    # Initialize WebDriver 
    try:
        driver = webdriver.Chrome()
    except Exception as e:
        print(f"Error initializing WebDriver. Ensure Chrome and ChromeDriver are correctly installed and matching versions. Error: {e}")
        return

    driver.get(FORM_URL)
    wait = WebDriverWait(driver, 15)
    print(f"Navigated to: {FORM_URL}")

    try:
        #  Handle Text/Short Answer
        print("Filling text inputs...")
        # Locating all common text input (type='text') and textarea fields
        text_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], textarea')

        for index, data in TEXT_INPUT_DATA.items():
            if index < len(text_inputs):
                field = text_inputs[index]
                # Scroll the element into view before interacting
                driver.execute_script("arguments[0].scrollIntoView(true);", field)
                field.send_keys(data)
                print(f"  -> Filled text input {index} with: '{data}'")
            else:
                print(f"  -> WARNING: Text input index {index} is out of range. Skipping.")

        # Handle Date of Birth Input
        print("\nFilling Date of Birth input...")
        try:
            # Locating the date input field 
            # The input requires a DD/MM/YYYY format string via send_keys.
            dob_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='date']")))
            
            # Argument changed to dob_input element for scrolling 
            driver.execute_script("arguments[0].scrollIntoView(true);", dob_input)
            
           
            dob_input.send_keys(DOB_DATA)
            
            print(f"  -> Filled Date of Birth with: '{DOB_DATA}'")
        except TimeoutException:
            print("  -> WARNING: Could not find Date of Birth input field. Skipping.")
        
        
        
        # 4. Submit the Form
        print("\nLocating and clicking Submit button...")
        submit_button_xpath = "//span[text()='Submit']/ancestor::div[@role='button']"
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))

        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        
       
        
        print("Successfully filled all fields and prepared to click the Submit button.")
        print("NOTE: The submit button click is currently commented out.")
        print(f"Pausing for 10 seconds to allow time for screenshot after submission.")
        print("Remember to check the live CAPTCHA code before submitting.")
        time.sleep(15)

    except Exception as e:
        print(f"\nAn unexpected error occurred during form filling: {e}")
        time.sleep(3)

    finally:
        print("\nClosing WebDriver.")
        driver.quit()

if __name__ == "__main__":
    fill_google_form()
