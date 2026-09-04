# Basic Unit Converter

**Basic Unit Converter** is a Python command-line application developed as a final project for **CS50's Introduction to Programming with Python (CS50P)**.

#### Video Demo

https://www.youtube.com/watch?v=ZCwjwMUAR9o

## Description

The **Basic Unit Converter** provides a simple and interactive way to convert numerical values between different units.

When the program starts, users can select a conversion category, choose the units they want to convert **from** and **to**, enter a value, and receive the converted result.

The application supports several commonly used conversion categories:

* Length
* Temperature
* Mass
* Area
* Volume
* Speed
* Time
* Digital Data

The project was created to apply Python programming concepts learned throughout CS50P, including **functions, loops, conditional statements, dictionaries, exception handling, input validation, and automated testing**.

## Features

* **Multiple Conversion Categories**
  Supports length, temperature, mass, area, volume, speed, time, and digital data conversions.

* **Interactive Command-Line Interface**
  Uses a menu-based interface to guide users through the conversion process.

* **Multiple Units**
  Provides several units within each supported category.

* **Accurate Conversions**
  Uses conversion factors and mathematical formulas appropriate for each category.

* **Temperature Conversion**
  Supports Celsius, Fahrenheit, and Kelvin conversions using temperature-specific formulas.

* **Input Validation**
  Handles invalid values and unsupported menu options.

* **Error Handling**
  Uses exception handling to prevent the program from terminating unexpectedly because of invalid input.

* **Continuous Conversions**
  Allows users to perform multiple conversions without restarting the program.

* **Clear Results**
  Displays the converted value in an easy-to-read format.

## Project Files

### `project.py`

The main Python program containing the application's core functionality. It includes:

* Conversion factors and unit dictionaries
* Conversion functions
* Temperature conversion formulas
* Input validation
* Error handling
* The `main()` function, which controls the command-line interface

### `test_project.py`

Contains automated tests written using **pytest** to verify the conversion functions and ensure that the program produces correct results for different conversion categories and input scenarios.

### `requirements.txt`

Lists the external Python package required to run the project's automated tests.

### `README.md`

Contains information about the project, its features, installation, usage, and implementation.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sij-an/cs50p-final-project.git
cd cs50p-final-project
```

## Usage

Run the program with:

```bash
python project.py
```

The program will display the available conversion categories and guide you through the conversion process.

## Testing

The project includes automated tests using **pytest**.

To run the tests:

```bash
pytest test_project.py
```


## Design and Implementation

The application uses Python dictionaries to organize units and their corresponding conversion factors. This allows conversions between units to be performed in a consistent and organized way.

Temperature conversions are handled separately because they require mathematical formulas rather than simple multiplication or division by a conversion factor.

The program is organized into separate functions for different tasks. This makes the code easier to understand, maintain, and test.

Input validation and exception handling are used to ensure that invalid user input is handled without causing the program to crash.

## What I Learned

Through this project, I applied the Python programming concepts covered in **CS50P** to create a practical command-line application.

The project helped me improve my understanding of:

* Writing and organizing functions
* Using dictionaries to store and access data
* Loops and conditional statements
* Exception handling with `try` and `except`
* Validating user input
* Writing automated tests with pytest
* Designing a command-line application
* Organizing a Python project

## Author

**Sijan Upreti**

T
