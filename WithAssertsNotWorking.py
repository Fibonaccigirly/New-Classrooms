"""Restful Booker Automated Testing"""
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

class YourTestCase(unittest.TestCase):

    def test_unexpected_success_content(self):
        # Test Case #1
        success_message = "Thanks for getting in touch Jane Doe!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Jane Doe!", "Unexpected success message content")

    def test_blank_name_error(self):
        # Test Case #2
        error_message = "Name may not be blank"
        self.assertEqual(error_message, "Name may not be blank", "Error message for blank name not found")

    def test_unexpected_success_content_2(self):
        # Test Case #3
        success_message = "Thanks for getting in touch Ñinä O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Ñinä O'Donell!", "Unexpected success message content")

    def test_timeout_error(self):
        # Test Case #4
        # Handle timeout   
              
    def test_invalid_email_format_error(self):
        # Test Case #5
        error_message = "must be a well-formed email address"
        self.assertEqual(error_message, "must be a well-formed email address", "Error message for invalid email format not found")

    def test_blank_email_error(self):
        # Test Case #6
        error_message = "Email may not be blank"
        self.assertEqual(error_message, "Email may not be blank", "Error message for blank email not found")

    def test_invalid_email_format_error_2(self):
        # Test Case #7
        error_message = "must be a well-formed email address"
        self.assertEqual(error_message, "must be a well-formed email address", "Error message for invalid email format not found")

    def test_unexpected_success_content_3(self):
        # Test Case #8
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_unexpected_success_content_4(self):
        # Test Case #9
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_phone_length_error(self):
        # Test Case #10
        error_message = "Phone must be between 11 and 21 characters."
        self.assertEqual(error_message, "Phone must be between 11 and 21 characters.", "Error message for phone length not found")

    def test_phone_length_error_2(self):
        # Test Case #11
        error_message = "Phone must be between 11 and 21 characters."
        self.assertEqual(error_message, "Phone must be between 11 and 21 characters.", "Error message for phone length not found")

    def test_blank_phone_error(self):
        # Test Case #12
        error_message = "Phone may not be blank"
        self.assertEqual(error_message, "Phone may not be blank", "Error message for blank phone not found")

    def test_unexpected_success_content_5(self):
        # Test Case #13
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_unexpected_success_content_6(self):
        # Test Case #14
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_subject_length_error(self):
        # Test Case #15
        error_message = "Subject must be between 5 and 100 characters."
        self.assertEqual(error_message, "Subject must be between 5 and 100 characters.", "Error message for subject length not found")

    def test_subject_length_error_2(self):
        # Test Case #16
        error_message = "Subject must be between 5 and 100 characters."
        self.assertEqual(error_message, "Subject must be between 5 and 100 characters.", "Error message for subject length not found")

    def test_unexpected_success_content_7(self):
        # Test Case #17
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_subject_length_error_3(self):
        # Test Case #18
        error_message = "Subject must be between 5 and 100 characters."
        self.assertEqual(error_message, "Subject must be between 5 and 100 characters.", "Error message for subject length not found")

    def test_unexpected_success_content_8(self):
        # Test Case #19
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_unexpected_success_content_9(self):
        # Test Case #20
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_message_length_error(self):
        # Test Case #21
        error_message = "Message must be between 20 and 2000 characters."
        self.assertEqual(error_message, "Message must be between 20 and 2000 characters.", "Error message for message length not found")

    def test_timeout_error_2(self):
        # Test Case #22
        # Handle timeout error assertion based on your testing framework

    def test_unexpected_success_content_10(self):
        # Test Case #23
        success_message = "Thanks for getting in touch Sam O'Donell!"
        self.assertNotEqual(success_message, "Thanks for getting in touch Sam O'Donell!", "Unexpected success message content")

    def test_message_length_error_2(self):
        # Test Case #24
        error_message = "Message must be between 20 and 2000 characters."
        self.assertEqual(error_message, "Message must be between 20 and 2000 characters.", "Error message for message length not found")


# Configure logging
logging.basicConfig(level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)


def fill_form_field(driver, field_id, field_value):
    #Fills in fields in the contact form
    try:
        field = driver.find_element(By.ID, field_id)
        field.clear()
        field.send_keys(field_value)
    except NoSuchElementException as exc:
        logging.error(f"Error filling form field: {exc}")

def submit_form(driver, button_id):
    try:
        submit_button = driver.find_element(By.ID, button_id)
        submit_button.click()
    except NoSuchElementException as exc:
        logging.error(f"Error submitting form: {exc}")

def get_message_xpath_for_iteration(iteration_number):
    # Simulating different XPaths for each iteration
    if iteration_number == 1:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 2:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 3:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 4:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 5:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 6:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 7:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 8:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 9:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 10:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 11:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 12:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 13:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 14:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 15:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 16:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 17:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 18:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 19:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 20:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 21:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 22:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    elif iteration_number == 23:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/div/h2'
    elif iteration_number == 24:
        return '//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]/p'
    else:
        return 'Invalid iteration number'


# Define test data for different variations of fields
form_variations = [
    {
       # positive test case
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "123-456-7890",
        "subject": "Inquiry",
        "description": "This is positive test data for all fields."
    },
    {
        # NAME FIELD
        # empty name field
        "name": "",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is an empty name field - neg."
    },
    {
        # special char in name field
        "name": "Ñinä O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is special char name field - pos"
    },
    {
        # many char in name field
        "name": "Adolph Blaine Charles David Earl Frederick Gerald Hubert Irvin John Kenneth Lloyd Martin Nero Oliver Paul Quincy Randolph Sherman Thomas Uncas Victor William Xerxes Yancy Zeus Wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswessenschafewarenwohlgepflegeundsorgfaltigkeitbeschutzenvonangreifendurchihrraubgierigfeindewelchevoralternzwolftausendjahresvorandieerscheinenvanderersteerdemenschderraumschiffgebrauchlichtalsseinursprungvonkraftgestartseinlangefahrthinzwischensternartigraumaufdersuchenachdiesternwelchegehabtbewohnbarplanetenkreisedrehensichundwohinderneurassevonverstandigmenschlichkeitkonntefortpflanzenundsicherfreuenanlebenslanglichfreudeundruhemitnichteinfurchtvorangreifenvonandererintelligentgeschopfsvonhinzwischensternartigraum",
        "email": "adolph@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is a very long name - edge"
    },
    {
        # EMAIL FIELD
        # badly formed email 
        "name": "Sam O'Donell",
        "email": "jane.example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is a badly formed email - neg"
    },
    {
        # empty email 
        "name": "Sam O'Donell",
        "email": "",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is an empty email - neg"
    },
    {
        # many char email 
        "name": "Sam O'Donell",
        "email": "contact-admin-hello-webmaster-info-services-peter-crazy-but-oh-so-ubber-cool-english-alphabet-loverer-abcdefghijklmnopqrstuvwxyz@please-try-to.send-me-an-email-if-you-can-possibly-begin-to-remember-this-coz.this-is-the-longest-email-address-known-to-man-but-to-be-honest.this-is-such-a-stupidly-long-sub-domain-it-could-go-on-foreverpacraig.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is a long email - edge"
    },
    {
        # PHONE TESTS
        # 11 char phone
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-321",
        "subject": "Feedback",
        "description": "This is 11 char phone - pos"
    },
    {
        # 21 char phone 
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210-1234-123",
        "subject": "Feedback",
        "description": "This is 21 char phone - pos"
    },
    {
        # more than 21 char phone
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "+1-555-123-4567-8901-2345-6789-0123-4",
        "subject": "Feedback",
        "description": "This is more than 21 char phone - edge "
    },
    {
        # fewer than 11 char phone
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654",
        "subject": "Feedback",
        "description": "This is fewer than 11 char phone - neg"
    },
    {
        # empty phone field
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "",
        "subject": "Feedback",
        "description": "This is an empty phone field - neg "
    },
    {
        # SUBJECT TESTS
        # 5 char subject
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Rooms",
        "description": "This is a 5 char subject - pos"
    },
    {
        # 100 char subject
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Availability Inquiry: Room Request Conference May 10 - Confirm Availability and Pricing Details Now!",
        "description": "This is 100 char subject - pos "
    },
    {
        # fewer than 5 char subject
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Help",
        "description": "This is fewer than 5 char subject - neg"
    },
    {
        # more than 100 char subject
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Subject: inquiry regarding availability for room reservation in connection with our conference scheduled for may 10 - kindly confirm the availability status and provide detailed pricing information.",
        "description": "This is more than 100 char subject - neg "
    },
    {
        # special char subject
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Inquiry About Rööm Bööking för Event Märch 5th ~ Seeking Availabilitÿ, Details, and Bööking Process.",
        "description": "This is special char subject - pos"
    },
    {
        # empty subject
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "",
        "description": "This is an empty subject - neg "
    },
    {
        # MESSAGE TESTS
        # 20 char message
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "This is 20 chars pos"
    },
    {
        # 2k char message
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"
    },
    {
        # fewer than 20 char message
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "Fewer than 20 - neg"
    },
    {
        # more than 2k char message
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodocupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo - edge"
    },
    {
        # special char message 
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": ("%Inquiry Regarding Rööm Bööking för Special Event ön Märch 5th ~\n\n"
                    "    Exploring Options för an Exclusive Gathering.\n"
                    "    Wöndering Aböut Availabilitÿ, Détails, and Facilities.\n"
                    "    Çould Yöu Share Insights and Guide Us in the Bööking Process?\n"
                    "    Grateful för Yöur Assistance! ', <, >, %")
    },
    {
        # empty char message
        "name": "Sam O'Donell",
        "email": "jane@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "description": ""
    },

    # Add more variations as needed
]

# Iterate through form variations
for i, variation in enumerate(form_variations, 1):
    # Create a new instance of the Chrome driver for each iteration
    driver = webdriver.Chrome()

    logging.info(f"Running test variation #{i}")

    # Navigate to the specified URL
    driver.get("https://automationintesting.online")

    # Add a short delay to allow the page to load completely
    time.sleep(2)

    # Fill each form field using the fill_form_field method
    for field_id, value in variation.items():
        fill_form_field(driver, field_id, value)

    # Click on the "submitContact" button using the submit_form method
    submit_form(driver, "submitContact")

    # Use WebDriverWait to wait for the success message element to appear
    try:
        success_message_xpath = get_message_xpath_for_iteration(i)
        success_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, success_message_xpath))
        )
        
    # Assert that the success message is not empty
    assert success_message_element.text.strip(), "Success message is empty"
    logging.info(f"Success message found: {success_message_element.text}")

    # Add assertions for the content of the success message
    if "Booking successful" in success_message_element.text:
        logging.info("Booking was successful")
    elif "Name may not be blank" in success_message_element.text:
        assert "Name may not be blank" in success_message_element.text, "Unexpected error message for blank name"
    elif "must be a well-formed email address" in success_message_element.text:
        assert "must be a well-formed email address" in success_message_element.text, "Unexpected error message for invalid email format"
    elif "Email may not be blank" in success_message_element.text:
        assert "Email may not be blank" in success_message_element.text, "Unexpected error message for blank email"
    elif "Phone must be between 11 and 21 characters." in success_message_element.text:
        assert "Phone must be between 11 and 21 characters." in success_message_element.text, "Unexpected error message for phone length"
    elif "Phone may not be blank" in success_message_element.text:
        assert "Phone may not be blank" in success_message_element.text, "Unexpected error message for blank phone"
    elif "Subject must be between 5 and 100 characters." in success_message_element.text:
        assert "Subject must be between 5 and 100 characters." in success_message_element.text, "Unexpected error message for subject length"
    elif "Message must be between 20 and 2000 characters." in success_message_element.text:
        assert "Message must be between 20 and 2000 characters." in success_message_element.text, "Unexpected error message for message length"
    else:
        assert False, "Unexpected success message content"

    # Handle TimeoutException if the success message does not appear within the specified time
    except TimeoutException:
        logging.error("Timed out waiting for success message to appear")

    # Add a delay (time can be adjusted as needed) before closing the browser
    time.sleep(2)

    # Close the browser window for each iteration
    try:
        driver.quit()
    except Exception as e:
        logging.error(f"Error closing the browser: {e}")