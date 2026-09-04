# Basic Unit Converter

#### Video Demo: https://www.youtube.com/watch?v=ZCwjwMUAR9o

#### Description:

The **Basic Unit Converter** is a Python command-line application developed as a final project for **CS50's Introduction to Programming with Python (CS50P)**. The purpose of this application is to provide a simple and user-friendly way to convert values between different units across multiple categories.

The application allows users to select a conversion category, choose the units they want to convert from and to, enter a value, and receive the converted result. It supports several commonly used categories, including **length, temperature, mass, area, volume, speed, time, and digital data**.

The project was designed to apply fundamental Python programming concepts learned throughout CS50P, including functions, loops, conditional statements, dictionaries, exception handling, user input validation, and modular program design.

---

### Core Features

1. **Multiple Conversion Categories**: Supports length, temperature, mass, area, volume, speed, time, and digital data conversions.
2. **Interactive Command-Line Interface**: Provides a simple menu-based interface that guides users through the conversion process.
3. **Multiple Units**: Each category includes multiple commonly used units for flexible conversions.
4. **Accurate Calculations**: Uses appropriate conversion factors and formulas for each supported unit.
5. **Temperature Conversion**: Supports conversions between Celsius, Fahrenheit, and Kelvin using the appropriate formulas.
6. **Input Validation**: Checks user input and handles invalid values and unsupported options.
7. **Error Handling**: Uses exception handling to prevent the program from crashing because of invalid input.
8. **Continuous Conversions**: Allows users to perform multiple conversions without restarting the application.
9. **Clear Output**: Displays the converted value in an easy-to-understand format.

---

### File Structure & Content Explanation

- **`project.py`**: Serves as the main program and contains the core functionality of the application. It defines:
  - Unit conversion dictionaries and conversion factors.
  - Functions responsible for performing conversions.
  - Temperature conversion formulas.
  - Input validation and error handling.
  - `main()`: Controls the interactive command-line interface, accepts user input, manages the conversion process, and displays the results.

- **`test_project.py`**: Contains automated tests using the `pytest` framework to verify the correctness of the conversion functions. The tests cover different conversion categories, unit conversions, temperature calculations, and invalid input scenarios.

- **`requirements.txt`**: Specifies the external Python packages required for the project and its tests.

- **`README.md`**: Provides an overview of the project, its features, implementation details, installation instructions, and usage information.

---

### Installation & Usage

1. **Clone the repository**:

   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```

2. **Install requirements**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python project.py
   ```

4. **Run unit tests**:

   ```bash
   pytest test_project.py
   ```

---

### Example

When the application starts, the user is presented with a list of available conversion categories.

For example, selecting **Length** allows the user to choose a source unit and a target unit, enter a numerical value, and receive the converted result.

The same process can be used for other categories such as **temperature, mass, area, volume, speed, time, and digital data**.

---

### Design & Implementation

The application uses Python dictionaries to organize supported units and their conversion factors. For conversions that require specific mathematical formulas, such as temperature, dedicated calculations are used.

The program is divided into functions so that different parts of the application can be handled independently. This makes the code easier to read, maintain, and test.

Input validation and exception handling are also used throughout the program to ensure that invalid user input is handled gracefully.

Through this project, I applied the Python programming concepts learned throughout **CS50P** to build a practical command-line application from scratch.
