# Beginner Python Programs

## Project Overview

This repository contains three Python programs that demonstrate basic Python programming concepts, including factorial calculation, Fibonacci series generation, and converting structured objects into dictionaries.

The programs are intended for beginners who want to practice functions, loops, recursion, classes, and dictionary operations.

## Programs Description

### 1. `factorial.py`

This program calculates the factorial of a non-negative integer using two approaches:

- **Iterative approach:** Uses a `for` loop to calculate the factorial.
- **Recursive approach:** Uses a function that calls itself to calculate the factorial.

Both functions raise a `ValueError` for negative numbers. The main program accepts an integer from the user, displays the results from both approaches, and handles `ValueError` exceptions.

### 2. `fibonacci.py`

This program works with Fibonacci numbers using two functions:

- **`fibonacci_series(n)`**: Returns a list containing the first `n` Fibonacci numbers. If `n` is zero or negative, it returns an empty list.
- **`nth_fibonacci(n)`**: Returns the Fibonacci number at the specified zero-based index. It raises a `ValueError` for negative indices.

The main program asks the user for the number of terms, displays the series, and displays the last requested term when the input is positive. It handles `ValueError` exceptions.

### 3. `structure_to_dict.py`

This program demonstrates four ways to convert structured data into dictionaries:

- **Dataclass conversion:** Uses `dataclasses.asdict()` to convert a `Student` dataclass object into a dictionary.
- **Object conversion:** Uses `vars()` to obtain the instance attributes of a regular `Book` class object as a dictionary.
- **Key-value pair conversion:** Uses `dict()` to convert a list of key-value tuples into a dictionary.
- **Student record conversion:** Converts a list of `Student` objects into a dictionary keyed by each student's roll number. Each value contains the student's name, branch, and marks.

The main program creates example objects and records, then prints the resulting dictionaries.

## Requirements

- Python 3
- No third-party packages are required by the provided code.
- The `dataclasses` module is imported by `structure_to_dict.py` and is part of the Python standard library.

## How to Run

Save all three Python files in the same directory as this `README.md`.

Open a terminal or command prompt in that directory and run the desired program.

### Run the factorial program

```bash
python factorial.py
```

### Run the Fibonacci program

```bash
python fibonacci.py
```

### Run the structure-to-dictionary program

```bash
python structure_to_dict.py
```

If your system uses `python3` as the command, replace `python` with `python3`.

## Learning Objectives

Through these programs, beginners can practice:

- Writing and calling Python functions.
- Using `for` loops and conditional statements.
- Understanding iterative and recursive approaches.
- Working with lists and dictionaries.
- Defining classes and creating objects.
- Using Python dataclasses.
- Converting objects and key-value pairs into dictionaries.
- Handling invalid input and `ValueError` exceptions.
- Organizing Python programs in a GitHub repository.

## Repository Structure

```text
.
├── factorial.py
├── fibonacci.py
├── structure_to_dict.py
└── README.md
```

## Conclusion

This repository demonstrates basic Python programming techniques through three small programs. It provides practice with mathematical calculations, sequence generation, object-oriented programming, dictionary conversion, and exception handling.
