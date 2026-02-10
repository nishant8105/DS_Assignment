# Employee Management System (EMS)

This project implements a simple **Employee Management System** in Python. It allows users to manage employee records using a command-line interface. The system stores employee data in a dictionary and provides options to add new employees, view all existing employees, and search for specific employees by their ID.

## Features

*   **Add Employee:** Allows the user to input details (ID, Name, Age, Department, Salary) for a new employee. It checks if the ID already exists to prevent duplicates.
*   **View All Employees:** Displays a formatted list of all employees currently in the system, including their ID, Name, Department, Age, and Salary.
*   **Search for Employee:** Enables the user to search for an employee using their unique Employee ID and displays their details if found.
*   **Exit:** Terminates the application.

## Data Structure

The system uses a nested dictionary to store employee information.
*   **Key:** Employee ID (integer)
*   **Value:** A dictionary containing the employee's details:
    *   `name` (String)
    *   `age` (Integer)
    *   `department` (String)
    *   `salary` (Integer/String)

### Initial Data
The system is pre-loaded with the following data:

| ID  | Name   | Age | Department | Salary |
| :-- | :----- | :-- | :--------- | :----- |
| 101 | Satya  | 27  | HR         | 50000  |
| 102 | Anjali | 30  | Finance    | 65000  |
| 103 | Ravi   | 25  | IT         | 70000  |
| 104 | Meena  | 29  | Marketing  | 55000  |

## Functions

### `menu()`
Displays the main menu options to the user and captures their choice.
*   **Returns:** The user's selected option as an integer.

### `Add_Employee()`
Prompts the user to enter a new Employee ID.
*   If the ID already exists, it asks the user to try again.
*   If the ID is new, it collects the employee's Name, Age, Department, and Salary, and adds the record to the `employees` dictionary.

### `View_all_Employees()`
Checks if there are any employees in the system.
*   If empty, it prints "No employee available".
*   If data exists, it prints a table header and iterates through the `employees` dictionary to display each employee's details in a formatted manner.

### `Search_Employee()`
Asks the user for an Employee ID.
*   Checks if the ID exists in the `employees` dictionary.
*   If found, prints the details of that employee.
*   If not found, informs the user.

## Usage

Run the script using a Python interpreter:

```bash
python main.py
```