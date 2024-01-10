Restful Booker Automated Testing

Introduction

This repository contains automated tests for a portion of the Restful Booker application. The purpose of these tests is to validate the application against specified requirements using End-to-End (E2E) testing. This README provides essential information about what was tested, how it was tested, any bugs found, and instructions on running the automated tests.

What Was Tested and How

Scope of Testing

I would normally approach the automation of booking tests by incorporating a data-driven approach, encompassing various start dates and durations. The automated tests would be designed to extract essential information, such as the number of nights and associated costs, from the screen. The goal would be to validate that the feature performs its intended function across diverse date ranges and data input.  
However, considering the substantial number of bugs uncovered during testing, along with the complexities of multi-selecting dates within the calendar, I made a deliberate decision to prioritize the automation of a fundamental scenario within the Booking Creation process. Additionally, in response to your specific requirement, a significant portion of my focus was dedicated to creating an automated test that completes the "Contact Us" form on the homepage.
The automation script, implemented in Python with Selenium, performs the following key steps:
- Navigates to the homepage.
- Locates the "Contact Us" form and fills it out with various data inputs, including different name variations, email addresses, and messages.
- Submits the form.
- Asserts the successful completion of the form submission by verifying the presence of a confirmation message or other success indicators.
This test not only demonstrates the capability to automate critical functionalities but also addresses a vital user interaction. It encompasses variations in the form inputs, including positive and edge cases such as a blank and special characters in input fields, to ensure a thorough validation of the "Contact Us" feature. 
The decision to focus on the "Contact Us" form allows for a more targeted approach. This strategic choice is driven by the current state of the features, with identified bugs influencing the decision not to conduct comprehensive automation at this stage. By prioritizing the "Contact Us" form and fundamental scenarios, this strategy aims to address critical aspects of the application while postponing broader automation efforts until the identified bugs are resolved. This methodological decision is rooted in the aim to balance the benefits of automation with the imperative for a stable foundation. It ensures that automated tests provide reliable results, contributing to a more robust and effective testing process as the features evolve.

Testing Tools and Framework

For this project, I opted to use Selenium IDE with Python 3.12.0 for several reasons:
- Ease of Use: Selenium IDE provides a user-friendly, record-and-playback interface that simplifies test script creation. This is particularly advantageous for quick test development and debugging.
- Python 3.12.0 Compatibility: Python is a versatile and widely-used programming language. The compatibility of Selenium IDE with Python 3.12.0 allows for leveraging the strengths of Python, such as readability and a vast array of libraries, in the testing process.
- Extensive Community Support: Selenium has a robust community with a wealth of documentation, forums, and resources. This ensures that any challenges encountered during the testing process can be addressed promptly through community support.
- Cross-Browser Compatibility: Selenium IDE supports testing across multiple browsers, ensuring that the application's functionality is consistent and reliable for users using different browsers.
- Flexibility for Future Enhancements: Selenium IDE, combined with Python, offers the flexibility to scale and enhance the test suite as the application evolves. The extensibility of Python allows for the integration of additional libraries or frameworks if required.
By choosing Selenium IDE with Python 3.12.0, I aimed to leverage a toolset that not only facilitates efficient test automation but also aligns with the specific needs and goals of this testing project.

Test Case Development

The test cases were created to address a crucial user interaction on the homepage: completing the "Contact Us" form. The primary objective of these automated tests is to simulate user behavior, ensuring that the form is filled out, submitted, and validating the successful completion of the form submission. Additionally, the tests aim to assess the application's response to various scenarios, including the correct and graceful error handling. 

The test cases cover a diverse range of scenarios, including:
- Navigation to the Homepage: Ensure the automated script navigates to the homepage successfully, setting the stage for the "Contact Us" form interaction.
- Form Completion with Various Inputs: Utilizing variations in the form data, including different name inputs, email addresses, and messages, the script fills out the "Contact Us" form. This step aims to encompass diverse scenarios, ensuring the resilience of the form to various inputs.
- Form Submission with Valid Data: The automated script submits the completed form with valid data, mimicking the user action in a successful scenario.
- Form Submission with Bad Data: Test the form's response to bad data by submitting the form with intentionally incorrect or invalid inputs, such as an invalid email address or phone number.
- Form Submission with No Data: Assess the form's behavior when submitted with empty fields, ensuring the appropriate handling of incomplete data.
- Assertion for Success (Commented Out): Due to the complexity of reliably identifying elements on the page after form submission, attempts to implement assertions verifying the success of each form submission have been made but were unsuccessful. Various approaches, including outerHTML, selectors, JS path, styles, XPath, and Full XPath, were explored, but unforeseen challenges were encountered. The absence of assertions in this case should be considered as a limitation in the current implementation.
By incorporating test cases with bad data and no data, the testing strategy extends to cover potential edge cases and error scenarios, contributing to a more thorough validation of the "Contact Us" form's functionality and user experience on the homepage.

Bugs Found

Bug Report 1: Unintuitive Room Booking Process
Summary: The process of booking a room is unintuitive.
Steps to Reproduce:
1. Navigate to the room booking section.
2. Attempt to select dates for booking.
Expected Behavior: Clear instructions on how to select dates for booking should be provided.
Actual Behavior: There is no indication that users must click and drag to select dates.

Bug Report 2: Lack of Feedback When Clicking on a Date in the Calendar
Summary: Clicking on a date in the calendar does not provide any error or helpful information.
Steps to Reproduce:
1. Attempt to click on a specific date in the calendar.
Expected Behavior: The system should respond with appropriate feedback or information letting the user know that they must click and drag *and* that there is a 2 day minimum.
Actual Behavior: No error or helpful information is displayed when clicking on a date in the calendar.

Bug Report 3: Unable to Unbook a Room
Summary: There is no indication or clear method to unbook a room once it has been reserved.
Steps to Reproduce:
1. Book a room.
2. Attempt to find a way to unbook or cancel the reservation.
Expected Behavior: A clear method to unbook or cancel a reservation should be provided.
Actual Behavior: There is no indication or clear method to unbook a room.

Bug Report 4: Data Entry Issue When Booking Again
Summary: The system does not recognize the user, requiring data entry for each booking.
Steps to Reproduce:
1. Attempt to make a new booking after a previous one.
2. Observe the system not recognizing the user.
Expected Behavior: User data should be retained for subsequent bookings.
Actual Behavior: The system does not recognize the user, and data must be entered again for each booking.

Bug Report 5: Lack of Real-time Validation for Subject Length Requirement
Summary: The Subject field lacks real-time validation, and users are not notified about the requirement for a length between 5 and 100 characters until after submitting the form.
Steps to Reproduce:
1. Navigate to the form containing the Subject field.
2. Enter a subject with a length outside the range of 5 to 100 characters.
3. Submit the form.
Expected Behavior: Real-time validation should inform users about the 5 to 100 characters requirement for the Subject field before attempting to submit the form.
Actual Behavior: The system does not provide real-time feedback to users about the required length for the Subject field. Users are only informed of the requirement after submitting the form, resulting in an error message.
Note: Implementing real-time validation for the Subject field will enhance the user experience by providing immediate feedback and preventing the submission of invalid data. This will help users adhere to the specified character count requirements.

Bug Report 6: Allowance for One-Night Booking Despite 2-Night Minimum Requirement
Summary: Users can book only one night, contrary to the established 2-night minimum requirement, and there is a lack of messaging indicating the minimum night stay.
Steps to Reproduce:
1. Attempt to book a stay for one night.
2. Observe the booking process.
3. Check for messaging regarding the 2-night minimum stay.
Expected Behavior: The booking process should clearly indicate the 2-night minimum requirement, and users should not be allowed to book for just one night.
Actual Behavior: Users are able to book only one night, and there is a lack of messaging informing them about the 2-night minimum stay requirement.
Note: It is crucial to address this issue by implementing a clear notification about the 2-night minimum stay requirement during the booking process. Additionally, the system should prevent users from successfully booking a stay for only one night. This will align with the established policy and avoid user confusion.

Bug Report 7: Difficulty Unselecting Dates
Summary: There is no apparent (simple) method to unselect dates once they are chosen.
Steps to Reproduce:
1. Select dates for booking.
2. Attempt to unselect or deselect the chosen dates.
Expected Behavior: There should be a straightforward way to unselect dates.
Actual Behavior: No simple method is provided to unselect dates; refreshing the page seems to be the only solution.

Bug Report 8: Multi-Selecting Entire Month Results in Incorrect Booking Period
Summary: Multi-selecting the entire month for booking includes dates beyond the visible screen.
Steps to Reproduce:
1. Attempt to book the entire month in the calendar.
2. Observe the booked period.
Expected Behavior: Booking should only include the dates visibly selected on the screen.
Actual Behavior: Multi-selecting the entire month results in a booking that includes dates beyond the visible screen.

Bug Report 9: Placeholder Text in Room Description
Summary: Room description contains Lorem Ipsum placeholder text, inconsistent with the rest of the English text on the platform.
Steps to Reproduce:
1. Navigate to the room description section.
2. Observe the content of the room description.
Expected Behavior: The room description should contain coherent and relevant information in English.
Actual Behavior: The room description contains Lorem Ipsum placeholder text, inconsistent with the rest of the English text.

Bug Report 10: Incorrect Night Count in Booking Confirmation
Summary: The booking confirmation displays an incorrect night count when selecting all available dates.
Steps to Reproduce:
1. Select all available dates from July 2024, from June 30th to August 3rd.
2. Review the booking confirmation details.
Expected Behavior: The booking confirmation should display the correct number of nights selected.
Actual Behavior: Although 35 nights are selected, the confirmation message states 34 nights. An additional day is added to the end of the booking period (June 30th to August 4th).
Screenshot Taken: <img width="659" alt="BugReportTen" src="https://github.com/Fibonaccigirly/New-Classrooms/assets/152340015/bbf6bc7d-2c55-4bcf-9b24-c685c2f93017">

Bug Report 11: Inconsistent and Non-Specific Field Length Error Messages
Summary: Error messages for field length do not provide specific information, and there is a discrepancy between the documented requirements and the actual behavior for the First Name field.
Steps to Reproduce:
1. Enter data into the name, email, and phone fields.
2. Intentionally provide data that does not meet the length requirements for the First Name field.
3. Observe the error messages.
Expected Behavior: Error messages should clearly indicate which field has a length issue and match the documented length requirements.
Actual Behavior: Error messages, such as "size must be between 3 and 18," are not specific about which field is causing the problem. The documented requirements for the First Name field specify a range of 3 to 20 characters. However, it appears that the First Name field only accepts up to 18 characters.
Discrepancy with Documentation:
First Name field character counts must be between 3 and 20 (documented requirement).
The observed behavior suggests that the First Name field only accepts up to 18 characters.


Bug Report 12: Incorrect Day Count in Message for One-Week Period
Summary: When selecting two or more dates within a one-week period that includes a Saturday, the displayed message about the number of days selected is incorrect.
Steps to Reproduce:
1. Select two or more dates in a one-week period that includes a Saturday (e.g., Fri and Sat or Thu, Fri, and Sat).
2. Observe the message indicating the number of nights selected.
Expected Behavior: The message should accurately reflect the number of nights selected, including the correct count when Saturdays are involved.
Actual Behavior: The message displays an incorrect count when selecting dates in a one-week period that includes a Saturday. For example:
Selecting Fri and Sat displays "1 night(s) selected."
Selecting Thu, Fri, and Sat displays "2 night(s) selected."
Note: Despite the incorrect message, the actual booking correctly reflects the accurate number of nights selected.


Bug Report 13: Ability to Select and Book Dates in the Past
Summary: The system allows users to select and book dates in the past.
Steps to Reproduce:
1. Navigate to the date selection section for booking.
2. Attempt to select and book dates that are in the past.
Expected Behavior: The system should prevent users from selecting and booking dates that have already passed.
Actual Behavior: Users are able to select and book dates that are in the past.
Note: Ensure that the system validates and restricts the selection of dates to the current date or any future dates. Users should not be able to book accommodations for dates that have already occurred.


Bug Report 14: Missing Requirement Information for Message Field
Summary: The Message field lacks information about the character count requirement (between 20 and 2000 characters), leading to form submission failures without prior notification.
Steps to Reproduce:
1. Navigate to the form containing the Message field.
2. Enter all required data 
Attempt to submit a message that does not meet the length requirements.
Expected Behavior: Users should be informed about the character count requirement for the Message field before attempting to submit the form.
Actual Behavior: The system does not provide information to users about the required character count range (20 to 2000) for the Message field. As a result, form submission fails without prior notification, leading to an error message.
Note: It is recommended to add a clear instruction or message near the Message field, notifying users about the required character count range to avoid submission errors.


Bug Report 15: Lack of User Notification for Phone Number Length Requirement
Summary: The phone number field lacks information about the requirement for an 11-digit number, and users are only informed of the requirement after submitting the form.
Steps to Reproduce:
1. Navigate to the form containing the phone number field.
2. Enter a phone number with a length other than 11 digits.
Submit the form.
Expected Behavior: Users should be notified about the 11-digit requirement for the phone number field before attempting to submit the form.
Actual Behavior: The system does not provide information to users about the required 11-digit length for the phone number field. Users are only informed of the requirement after submitting the form, resulting in an error message.
Note: To enhance user experience, it is recommended to implement real-time validation or provide clear instructions near the phone number field, indicating the specific requirements to avoid submission errors.


Bug Report 17: Layout Issue with Maximum Character Count in Subject Field
Summary: When using the maximum character count in the Subject field, the resulting page displays the subject text across the screen, causing overlap with the contact information for the B&B.
Steps to Reproduce:
1. Navigate to the form containing the Subject field.
2. Enter text in the Subject field with the maximum character count.
3. Submit the form and observe the resulting page layout.
Expected Behavior: The layout of the resulting page should accommodate the entered subject text, preventing overlap with other elements.
Actual Behavior: When using the maximum character count in the Subject field, the subject text spans across the screen, causing overlap with the contact information for the B&B.
Note: It is recommended to adjust the layout or provide a mechanism to handle long subject text gracefully, ensuring it does not interfere with other elements on the page. This will enhance the overall presentation and readability of the content.


Bug Report 18: Inconsistency in Location Name
Summary: There is an inconsistency in the location name provided by the introduction message and the address listed next to the Contact form.
Steps to Reproduce:
1. Read the introduction message for location information.
2. Compare the location name in the introduction message with the address listed next to the Contact form.
Expected Behavior: The location name should be consistent in both the introduction message and the address details.
Actual Behavior: The introduction message mentions "Newingtonfordburyshire," while the address listed next to the Contact form mentions "Newfordburyshire," indicating an inconsistency in the location name.
Note: Ensuring consistency in location information will prevent confusion for users and provide accurate details about the B&B's location. It is recommended to update either the introduction message or the address details to maintain coherence.


Automated Testing Project

This project focuses on automating the "Contact Us" form on the homepage using Selenium in Visual Studio Code with Python.

Stack Used:

- Selenium WebDriver
- Visual Studio Code (VS Code)
- Python 3.12.0
- 
Instructions for Running the Project:

Prerequisites:
- Ensure you have Python installed on your machine. You can download it here: https://www.python.org/downloads/
- Install the necessary Python packages using the following command in your terminal:

%pip install selenium

Running the Automated Tests:

To run the automated tests on your local machine, follow these instructions:

1. Clone the Repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository

2. Open the Project in Visual Studio Code:

code .

3. Run the Automated Tests:

- Open the Python script containing your automated tests (e.g., contact_us_test.py) in VS Code.
- Execute the script by using the VS Code debugger or running the following command in the terminal:

python contact_us_test.py

4. View Test Results:

- The terminal will display the progress and results of the automated tests.
- Any encountered errors or exceptions will be logged for further analysis.

Notes:

- Make sure to have the appropriate web drivers (e.g., ChromeDriver) in your system PATH or provide the path explicitly in your script.
- Adjust the script according to your file structure and naming conventions.

By following these instructions, you should be able to run the automated tests successfully on your local machine.

Conclusion

This automated testing project aims to ensure the reliability and functionality of the Restful Booker application. The identified bugs and testing process details are provided to facilitate understanding and further improvements.

