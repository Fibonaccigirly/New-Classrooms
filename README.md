# New Classrooms Restful Booker Automated Testing

## Introduction

This repository contains automated tests for a portion of the Restful Booker application. The purpose of these tests is to validate the application against specified requirements using End-to-End (E2E) testing. This README provides essential information about what was tested, how it was tested, any bugs found, and instructions on running the automated tests.

## What Was Tested and How

### Scope of Testing

I would normally approach the automation of booking tests by incorporating a data-driven approach, encompassing various start dates and durations. The automated tests would be designed to extract essential information, such as the number of nights and associated costs, from the screen. The goal would be to validate that the feature performs its intended function across diverse date ranges and data input insuring the full functionality of the booking feature. 

Given the considerable number of bugs uncovered during testing and the intricacies of multi-selecting dates within the calendar, I made a deliberate decision to prioritize the automation of a singular fundamental scenario. Specifically, my focus was on creating automated tests that not only navigate and complete the "Contact Us" form on the homepage but also rigorously assess its functionality under various conditions.

The automation script, implemented in Python with Selenium, performs the following key steps:
- Navigates to the homepage.
- Locates the "Contact Us" form and fills it out with various data inputs, including different name variations, email addresses, and messages.
- Submits the form.
- Validates the successful completion of the Contact Us form submission by verifying the presence of a confirmation message as the indicator of success. 
These tests encompasse variations in the form inputs, including positive and negative as well as edge cases such as blank and special characters in input fields.
My decision to prioritize the automation of the "Contact Us" form was guided by the principle that even if other features encountered issues, customers could still reach out for assistance. This approach aligns with the notion of ensuring a direct line of communication with users. In essence, it reflects the sentiment: "First thing I'm going to do is make sure the phones work."

### Testing Tools and Framework

For this project, I chose to use Selenium IDE with Python 3.12.0 for several reasons:
- **Ease of Use:** Selenium IDE provides a user-friendly environment for testing web applications.
- **Python 3.12.0 Compatibility:** Python is a versatile and widely-used programming language. The compatibility of Selenium IDE with Python 3.12.0 allows for leveraging the strengths of Python, such as readability and a vast array of libraries, in the testing process.
- **Extensive Community Support:** Selenium has a robust community with a wealth of documentation, forums, and resources. This ensures that any challenges encountered during the coding process can be addressed promptly leveraging community support.
- **Cross-Browser Compatibility:** Selenium IDE supports testing across multiple browsers, ensuring that the application's functionality is consistent and reliable for users using different browsers.
- **Flexibility for Future Enhancements:** Selenium IDE, combined with Python, offers the flexibility to scale and enhance the test suite as the application evolves. The extensibility of Python allows for the integration of additional libraries or frameworks if required.
By choosing Selenium IDE with Python 3.12.0, I aimed to leverage a toolset that not only facilitates efficient test automation but also aligns with the specific needs and goals of this testing project.

### Test Case Development

The test cases were created to address a crucial user interaction on the homepage: completing the "Contact Us" form. The primary objective of these automated tests is to simulate user behavior, ensuring that the form is filled out, submitted, and validating the successful completion of the form submission. Additionally, the tests assess the application's response to various scenarios, including the correct inputs and graceful error handling. 

The test cases cover a diverse range of scenarios, including:
- **Navigation to the Homepage:** Ensure the automated script navigates to the homepage successfully, setting the stage for the "Contact Us" form interaction.
- **Form Completion with Various Inputs:** Utilizing variations in the form data, including different name inputs, email addresses, and messages, the script fills out the "Contact Us" form. This step aims to encompass diverse scenarios, ensuring the resilience of the form to invalid inputs.
  - _Form Submission with Valid Data:_ The automated script submits the completed form with valid data, mimicking the user action in a successful scenario.
  - _Form Submission with Bad Data:_ Test the form's response to bad data by submitting the form with intentionally incorrect or invalid inputs, such as an invalid email address or phone number.
  - _Form Submission with No Data:_ Assess the form's behavior when submitted with empty fields, ensuring the appropriate handling of incomplete data.
- **Assertion for Success:** Assertions for success have been implemented using various possible approaches which could include, outerHTML, selectors, JS path, styles, XPath, or Full XPath, to reliably identify elements on the page after form submission. These assertions play a crucial role in validating the form's functionality. The testing strategy is extended by including test cases with both bad data and no data, covering potential edge cases and error scenarios.

## Bugs Found

## BR 1: Unintuitive Room Booking Process

**Summary:** The process of booking a room is unintuitive.

**Steps to Reproduce:**
1. Navigate to the room booking section.
2. Attempt to select dates for booking.
   
**Expected Behavior:** Clear instructions on how to select dates for booking should be provided.

**Actual Behavior:** There is no indication that users must click and drag to select dates.

---

## BR 2: Lack of Feedback When Clicking on a Date in the Calendar

**Summary:** Clicking on a date in the calendar does not provide any error or helpful information.

**Steps to Reproduce:**
1. Attempt to click on a specific date in the calendar.
   
**Expected Behavior:** The system should respond with appropriate feedback or information letting the user know that they must click and drag *and* that there is a 2 day minimum.

**Actual Behavior:** No error or helpful information is displayed when clicking on a date in the calendar.

---

## BR 3: Unable to Unbook a Room

**Summary:** There is no indication or clear method to unbook a room once it has been reserved.

**Steps to Reproduce:**
1. Book a room.
2. Attempt to find a way to unbook or cancel the reservation.

**Expected Behavior:** A clear method to unbook or cancel a reservation should be provided.

**Actual Behavior:** There is no indication or clear method to unbook a room.

...

---

## BR 18: Inconsistency in Location Name

**Summary:** There is an inconsistency in the location name provided by the introduction message and the address listed next to the Contact form.

**Steps to Reproduce:**
1. Read the introduction message for location information.
2. Compare the location name in the introduction message with the address listed next to the Contact form.

**Expected Behavior:** The location name should be consistent in both the introduction message and the address details.

**Actual Behavior:** The introduction message mentions "Newingtonfordburyshire," while the address listed next to the Contact form mentions "Newfordburyshire," indicating an inconsistency in the location name.

...

---

##BR 19: **Form Submission Failure with Excessively Long Names

**Summary:** Submitting the Contact Us form with excessively long first and last names results in a blank page, and the form does not recover.

**Steps to Reproduce:**
1. Navigate to the Contact Us form.
2. Enter the following first/last name:
  - First: Adolph Blaine Charles David Earl Frederick Gerald Hubert Irvin John Kenneth Lloyd Martin Nero Oliver Paul Quincy Randolph Sherman Thomas Uncas Victor William Xerxes Yancy Zeus 
  - Last: Wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswessenschafewarenwohlgepflegeundsorgfaltigkeitbeschutzenvonangreifendurchihrraubgierigfeindewelchevoralternzwolftausendjahresvorandieerscheinenvanderersteerdemenschderraumschiffgebrauchlichtalsseinursprungvonkraftgestartseinlangefahrthinzwischensternartigraumaufdersuchenachdiesternwelchegehabtbewohnbarplanetenkreisedrehensichundwohinderneurassevonverstandigmenschlichkeitkonntefortpflanzenundsicherfreuenanlebenslanglichfreudeundruhemitnichteinfurchtvorangreifenvonandererintelligentgeschopfsvonhinzwischensternartigraum
3. Submit the form.
4. Observe the result.

**Expected Behavior:** The system should handle long names gracefully, providing appropriate error messages or preventing submission, but not resulting in a blank page.

**Actual Behavior:** Submitting the form with the given extremely long names leads to a blank page, and the form does not recover.

**Note:** To enhance the robustness of the form submission process, it is recommended to implement validation checks on the length of the entered names and provide clear error messages to users when the data exceeds acceptable limits. This will prevent issues such as blank pages and improve the overall user experience.



## Automated Testing Project

This project focuses on automating the "Contact Us" form on the homepage using Selenium in Visual Studio Code with Python.

### Stack Used:

- Selenium WebDriver
- Visual Studio Code (VS Code)
- Python 3.12.0
- 
### Instructions for Running the Project:

**Prerequisites:**
- Ensure you have Python installed on your machine. You can download it here: https://www.python.org/downloads/
- Install the necessary Python packages using the following command in your terminal:

`%pip install selenium`

**Running the Automated Tests:**

To run the automated tests on your local machine, follow these instructions:

**1. Clone the Repository:**

`git clone https://github.com/Fibonaccigirly/New-Classrooms.git
cd New-Classrooms`

**2. Open the Project in Visual Studio Code:**

`code .`

**3. Run the Automated Tests:**

- Open the Python script containing your automated tests (e.g., contact_us_test.py) in VS Code.
- Execute the script by using the VS Code debugger or running the following command in the terminal:

`python NewClassroomsBookerTest.py`

**4. View Test Results:**

- The terminal will display the progress and results of the automated tests.
- Any encountered errors or exceptions will be logged for further analysis.

## Notes:

- Make sure to have the appropriate web drivers (e.g., ChromeDriver) in your system PATH or provide the path explicitly in your script.
- Adjust the script according to your file structure and naming conventions.

By following these instructions, you should be able to run the automated tests successfully on your local machine.



## Assumptions and Considerations:

During the testing process, certain assumptions were made to guide the test scenarios. These assumptions are detailed below:

1. Email:

  - Ill-formed email:
    - Assumption: The application is expected to perform validation on the email field to ensure it adheres to a standard email format.
  - Empty email:
    - Assumption: The Email field is assumed to be a required field, and an empty email is considered an invalid input.
  - Long email:
    - Assumption: The application is assumed to handle emails up to the specified maximum character limit, and exceeding this limit may result in an error or truncation.

2. Phone:

  - 11 characters:
    - Assumption: The application is expected to accept a phone number with exactly 11 characters as a valid input.
  - 21 characters:
    - Assumption: The application is expected to accept a phone number with exactly 21 characters as a valid input.
  - More than 21 characters:
    - Assumption: Exceeding the specified maximum character limit for the phone number may result in an error or truncation.
  - Fewer than 11 characters:
    - Assumption: The application is expected to reject phone numbers with fewer than 11 characters as invalid inputs.
  - Empty phone field:
    - Assumption: The Phone field is assumed to be required, and leaving it blank is considered an invalid input.

3. Subject:

  - 5 characters:
    - Assumption: The application is expected to accept a subject with exactly 5 characters as a valid input.
  - 100 characters:
    -Assumption: The application is expected to accept a subject with exactly 100 characters as a valid input.
  - Fewer than 5 characters:
    - Assumption: Subjects with fewer than 5 characters are assumed to be rejected as invalid inputs.
  - More than 100 characters:
    - Assumption: Exceeding the specified maximum character limit for the subject may result in an error or truncation.
  - Special characters:
    - Assumption: The application is assumed to reject subjects containing special characters as invalid inputs.
  - Empty subject:
    - Assumption: The Subject field is assumed to be required, and leaving it blank is considered an invalid input.

4. Message:

  - 20 characters:
    - Assumption: The application is expected to accept a message with exactly 20 characters as a valid input.
  - 2000 characters:
    - Assumption: The application is expected to accept a message with exactly 2000 characters as a valid input.
  - Less than 20 characters:
    - Assumption: Messages with fewer than 20 characters are assumed to be rejected as invalid inputs.
  - More than 2000 characters:
    - Assumption: Exceeding the specified maximum character limit for the message may result in an error or truncation.
  - Special characters:
    - Assumption: The application is assumed to reject messages containing special characters as invalid inputs.
  - Empty message:
    - Assumption: The Message field is assumed to be required, and leaving it blank is considered an invalid input.

## Conclusion

This automated testing project ensures the reliability and functionality of the Restful Booker application. The identified bugs and testing process details are provided to facilitate understanding for future improvement.

