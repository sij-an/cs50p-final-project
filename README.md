# Basic Unit Converter

#### Video Demo: https://www.youtube.com/watch?v=ZCwjwMUAR9o

## Description

Basic Unit Converter is a Python command-line program that converts values between different units. The program first asks the user what type of conversion they want to perform, then asks for the original unit, the target unit, and the value to convert. It then calculates and displays the converted value.

The purpose of this project is to provide a simple and easy-to-use converter that supports multiple types of measurements in one program. Instead of having separate programs for different conversions, the user can select the required category and perform the conversion from the same interface.

## Features

The converter currently supports the following categories:

* Length
* Temperature
* Mass
* Area
* Volume
* Speed
* Time
* Digital Data

For each category, the program provides several units that the user can convert between.

## Project Files

### `project.py`

This is the main program. It contains the conversion functions for each category and the main program logic that interacts with the user.

The program takes user input, validates the selected conversion category and units, performs the required calculation, and displays the result.

### `test_project.py`

This file contains tests for the conversion functions in `project.py`. The tests help verify that the calculations produce the expected results for different units and values.

## How to Run

Make sure Python 3 is installed on your computer.

Clone or download this repository and open the project directory in a terminal.

Run the program with:

```bash
python3 project.py
```

The program will then guide you through the conversion process.

## How to Use

After starting the program:

1. Select a conversion category.
2. Select the unit you want to convert from.
3. Select the unit you want to convert to.
4. Enter the value you want to convert.
5. The program displays the converted value.

For example, a user can select **Length**, choose **meters** as the original unit, choose **kilometers** as the target unit, and enter a value. The program will then display the equivalent value in kilometers.

## Testing

The project includes `test_project.py` to test the conversion functions.

The tests can be run using:

```bash
pytest test_project.py
```

The tests check different conversion categories and help ensure that the conversion calculations work correctly.

## Design

I designed the program using separate functions for different types of conversions. This makes the code easier to understand, test, and modify. Each conversion function is responsible for a specific category rather than putting all conversion logic into one large function.

I also used dictionaries to store unit conversion factors where appropriate. This allows the program to support multiple units without having to write a separate calculation for every possible pair of units.

The main program handles user interaction and decides which conversion function should be used based on the category selected by the user. This separation between user interaction and conversion logic makes the program more organized and maintainable.

Input validation is also included so that invalid choices do not immediately cause the program to crash. The user is prompted to provide valid input before the conversion is performed.

## What I Learned

While building this project, I practiced using functions, loops, conditionals, dictionaries, exception handling, user input, and testing in Python. I also learned more about organizing a larger Python program into separate functions and testing individual parts of the program.

This project helped me understand how the concepts learned throughout CS50P can be combined to create a complete command-line application.

## Author

**Sijan Upreti**

This project was created as my final project for **CS50's Introduction to Programming with Python (CS50P)**.
