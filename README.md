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

### BR 1: Unintuitive Room Booking Process

**Summary:** The process of booking a room is unintuitive.

**Steps to Reproduce:**
1. Navigate to the room booking section.
2. Attempt to select dates for booking.
   
**Expected Behavior:** Clear instructions on how to select dates for booking should be provided.

**Actual Behavior:** There is no indication that users must click and drag to select dates.

---

### BR 2: Lack of Feedback When Clicking on a Date in the Calendar

**Summary:** Clicking on a date in the calendar does not provide any error or helpful information.

**Steps to Reproduce:**
1. Attempt to click on a specific date in the calendar.
   
**Expected Behavior:** The system should respond with appropriate feedback or information letting the user know that they must click and drag *and* that there is a 2 day minimum.

**Actual Behavior:** No error or helpful information is displayed when clicking on a date in the calendar.

---

### BR 3: Unable to Unbook a Room

**Summary:** There is no indication or clear method to unbook a room once it has been reserved.

**Steps to Reproduce:**
1. Book a room.
2. Attempt to find a way to unbook or cancel the reservation.

**Expected Behavior:** A clear method to unbook or cancel a reservation should be provided.

**Actual Behavior:** There is no indication or clear method to unbook a room.

---

### BR 4: Data Entry Issue When Booking Again

**Summary:** The system does not recognize the user, requiring data entry for each booking.

**Steps to Reproduce:**
1. Attempt to make a new booking after a previous one.
2. Observe the system not recognizing the user.

**Expected Behavior:** User data should be retained for subsequent bookings.

**Actual Behavior:** The system does not recognize the user, and data must be entered again for each booking.

---

### BR 5: Lack of Real-time Validation for All Fields

**Summary:** The system lacks real-time validation for all fields, and users aren't notified about the requirements during data entry.

**Steps to Reproduce:**
1. Navigate to the form containing the Subject field.
2. Enter text in the Subject field with the maximum character count.
3. Submit the form and observe the resulting page layout.

**Expected Behavior:** Real-time validation should inform users about the specified requirements for each field as they enter data, preventing the submission of invalid entries.

**Actual Behavior:** The system does not provide real-time feedback to users about the required validation for any field during data entry. Users are only informed of the requirements after submitting the form, resulting in an error message.

**Note:** Implementing real-time validation for all fields will enhance the user experience by providing immediate feedback during data entry and preventing the submission of invalid data. This will help users adhere to the specified requirements.

---

### BR 6: Allowance for One-Night Booking Despite 2-Night Minimum Requirement

**Summary:** Users can book only one night, contrary to the established 2-night minimum requirement, and there is a lack of messaging indicating the minimum night stay.

**Steps to Reproduce:**
1. Attempt to book a stay for one night.
2. Observe the booking process.
3. Check for messaging regarding the 2-night minimum stay.

**Expected Behavior:** The booking process should clearly indicate the 2-night minimum requirement, and users should not be allowed to book for just one night.

**Actual Behavior:** Users are able to book only one night, and there is a lack of messaging informing them about the 2-night minimum stay requirement.

**Note:** It is crucial to address this issue by implementing a clear notification about the 2-night minimum stay requirement during the booking process. Additionally, the system should prevent users from successfully booking a stay for only one night. This will align with the established policy and avoid user confusion.

---

### BR 7: Difficulty Unselecting Dates

**Summary:** There is no apparent (simple) method to unselect dates once they are chosen.

**Steps to Reproduce:**
1. Select dates for booking.
2. Attempt to unselect or deselect the chosen dates.

**Expected Behavior:** There should be a straightforward way to unselect dates.

**Actual Behavior:** No simple method is provided to unselect dates; either selecting additional days or refreshing the page works

---

### BR 8: Multi-Selecting Entire Month Results in Incorrect Booking Period

**Summary:** Multi-selecting the entire month for booking includes dates beyond the visible screen.

**Steps to Reproduce:**
1. Attempt to book the entire month in the calendar.
2. Observe the booked period.

**Expected Behavior:** Booking should only include the dates visibly selected on the screen.

**Actual Behavior:** Multi-selecting the entire month results in a booking that includes dates beyond the visible screen.

---

### BR 9: Placeholder Text in Room Description

**Summary:** Room description contains Lorem Ipsum placeholder text, inconsistent with the rest of the English text on the platform.

**Steps to Reproduce:**
1. Navigate to the room description section.
2. Observe the content of the room description.

**Expected Behavior:** The room description should contain coherent and relevant information in English.

**Actual Behavior:** The room description contains Lorem Ipsum placeholder text, inconsistent with the rest of the English text.

---

### BR 10: Incorrect Night Count in Booking Confirmation

**Summary:** The booking confirmation displays an incorrect night count when selecting dates.

**Steps to Reproduce:**
1. Select several available dates
2. Review the booking confirmation details

**Expected Behavior:** The booking confirmation should display the correct number of nights selected.

**Actual Behavior:** When selecting mutltiple dates it seems to drop one of the days

<img width="700" alt="Screen Shot 2024-01-11 at 3 32 52 PM" src="https://github.com/Fibonaccigirly/New-Classrooms/assets/152340015/eed52d8c-bb99-4124-bebe-f2d49fc8958b">


---

### BR 11: Inconsistent and Non-Specific Field Length Error Messages

**Summary:** Error messages for field length do not provide specific information, and there is a discrepancy between the documented requirements and the actual behavior for the First Name field.

**Steps to Reproduce:**
1. Enter data into the name, email, and phone fields.
2. Intentionally provide data that does not meet the length requirements for the First Name field.
3. Observe the error messages.

**Expected Behavior:** Error messages should clearly indicate which field has a length issue and match the documented length requirements.

**Actual Behavior:** Error messages, such as "size must be between 3 and 18," are not specific about which field is causing the problem. The documented requirements for the First Name field specify a range of 3 to 20 characters. However, it appears that the First Name field only accepts up to 18 characters.

**Discrepancy with Documentation:**
First Name field character counts must be between 3 and 20 (documented requirement).
The observed behavior suggests that the First Name field only accepts up to 18 characters.

---

### BR 12: Ability to Select and Book Dates in the Past

**Summary:** The system allows users to select and book dates in the past.

**Steps to Reproduce:**
1. Navigate to the date selection section for booking.
2. Attempt to select and book dates that are in the past.

**Expected Behavior:** The system should prevent users from selecting and booking dates that have already passed.

**Actual Behavior:** Users are able to select and book dates that are in the past.

**Note:** Ensure that the system validates and restricts the selection of dates to the current date or any future dates. Users should not be able to book accommodations for dates that have already occurred.
Today's date is January 11th 2024: 
<img width="680" alt="Screen Shot 2024-01-11 at 3 35 30 PM" src="https://github.com/Fibonaccigirly/New-Classrooms/assets/152340015/504740fc-dce3-4e4b-85de-053d1ce54b71">

---

### BR 13: Layout Issue with Maximum Character Count in Subject Field

**Summary:** When using the maximum character count in the Subject field, the resulting page displays the subject text across the screen, causing overlap with the contact information for the B&B.

**Steps to Reproduce:**
1. Navigate to the form containing the Subject field.
2. Enter text in the Subject field with the maximum character count.
3. Submit the form and observe the resulting page layout.

**Expected Behavior:** The layout of the resulting page should accommodate the entered subject text, preventing overlap with other elements.

**Actual Behavior:** When using the maximum character count in the Subject field, the subject text spans across the screen, causing overlap with the contact information for the B&B.

**Note:** It is recommended to adjust the layout or provide a mechanism to handle long subject text gracefully, ensuring it does not interfere with other elements on the page. This will enhance the overall presentation and readability of the content.

---

### BR 14: Inconsistency in Location Name

**Summary:** There is an inconsistency in the location name provided by the introduction message and the address listed next to the Contact form.

**Steps to Reproduce:**
1. Read the introduction message for location information.
2. Compare the location name in the introduction message with the address listed next to the Contact form.

**Expected Behavior:** The location name should be consistent in both the introduction message and the address details.

**Actual Behavior:** The introduction message mentions "Newingtonfordburyshire," while the address listed next to the Contact form mentions "Newfordburyshire," indicating an inconsistency in the location name.

**Note:** Ensuring consistency in location information will prevent confusion for users and provide accurate details about the B&B's location. It is recommended to update either the introduction message or the address details to maintain coherence.

---

### BR 15: Form Submission Failure with Excessively Long Names

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

---

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

