
# Student Performance Analyzer

A simple desktop graphical user interface (GUI) application built with Python and Tkinter. This tool allows users to input student marks for four core subjects and instantly calculates the total marks, overall percentage, final grade, and pass/fail status.

## Features

* **User-Friendly GUI:** Clean, centered interface with a cohesive color scheme.
* **Input Validation:** Ensures that users enter valid numeric marks between 0 and 100. Displays error dialogs for invalid inputs.
* **Automated Calculations:** Calculates total marks (out of 400) and exact percentages.
* **Strict Pass/Fail Logic:** Automatically marks a student as "FAIL" if they score below 35 in *any* single subject, regardless of their total percentage.
* **Letter Grading:** Assigns a specific letter grade based on the student's percentage.
* **Quick Reset:** Includes a "Clear" button to easily erase all inputs and results for a new calculation.

## Prerequisites

To run this application, you need to have Python installed on your computer.

* **Python 3.x**
* **Tkinter:** This is the standard GUI library for Python. It is typically included by default with standard Python installations, so no additional installation via `pip` is required.

## How to Run

1. Download or save the provided Python script as `Student-performance-analyzer.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Execute the following command:

   ```bash
   python Student-performance-analyzer.py
   ```

   *(Note: Depending on your system configuration, you might need to use `python3` instead of `python`)*

## Usage

1. Launch the application.
2. Enter the marks (out of 100) for Physics, Chemistry, Mathematics, and English in the respective input boxes.
3. Click the **Calculate Result** button.
4. The application will display the Total, Percentage, Grade, and Result (PASS/FAIL) at the bottom of the window.
5. Click the **Clear** button to reset the form and enter new marks.

## Grading Criteria

The application uses the following logic to assign grades and results:

**Passing Criteria:**
* A student must score a minimum of 35 marks in **every** subject to pass.
* If any subject's mark is < 35, the overall result is **FAIL** and the grade is **F**.

**Grade Scale (If Passed):**
* **90% and above:** A+
* **80% to 89.99%:** A
* **70% to 79.99%:** B
* **60% to 69.99%:** C
* **50% to 59.99%:** D
* **35% to 49.99%:** E
