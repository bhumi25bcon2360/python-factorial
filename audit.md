# Code and README Audit Report

## 1. Audit Overview

This audit reviews the Python source code and project documentation to determine whether the implemented functionality is correctly described, identify potential limitations, and suggest improvements.

The audit covers `factorial.py`, `fibonacci.py`, `structure_to_dict.py`, and `README.md`.

The findings are based on source-code inspection. No claim is made that the programs have been executed or tested.

## 2. Files Reviewed

| File | Purpose |
|---|---|
| `factorial.py` | Calculates factorials using iterative and recursive methods. |
| `fibonacci.py` | Generates Fibonacci series and calculates a Fibonacci number using zero-based indexing. |
| `structure_to_dict.py` | Demonstrates converting dataclass instances, objects, key-value pairs, and student records into dictionaries. |
| `README.md` | Documents the project, its requirements, execution commands, and learning objectives. |

## 3. Code Audit Findings

### 3.1 `factorial.py`

**Implemented functionality**

- `factorial_iterative(n)` calculates a factorial using a loop.
- `factorial_recursive(n)` calculates a factorial using recursion.
- Both functions raise `ValueError` when the input is negative.
- The main program accepts an integer and displays the results from both methods.
- The program catches `ValueError` exceptions and displays an error message.

**Correctness observations**

The iterative implementation initializes `result` to `1` and multiplies it by the integers from `2` through `n`. The recursive implementation returns `1` for `0` and `1`, and otherwise multiplies `n` by the factorial of `n - 1`.

Both approaches correctly handle the mathematical base cases, including `0! = 1`.

**Potential limitations**

- The recursive method can raise `RecursionError` for sufficiently large inputs because of Python's recursion limit.
- Very large factorials can require substantial computation and memory.
- The function annotations indicate integer inputs, but Python does not automatically enforce those annotations at runtime.

**Recommendations**

- Add tests for `0`, `1`, a positive integer, and a negative integer.
- Consider documenting the recursion limitation.
- If very large inputs are expected, prefer the iterative implementation.

### 3.2 `fibonacci.py`

**Implemented functionality**

- `fibonacci_series(n)` returns the first `n` Fibonacci numbers.
- `nth_fibonacci(n)` calculates the Fibonacci number at a zero-based index.
- Negative indices passed to `nth_fibonacci()` raise `ValueError`.
- The main program accepts the requested number of terms, displays the series, and prints the final requested term when the input is positive.

**Correctness observations**

The series begins with `0` and follows the sequence `0, 1, 1, 2, 3, ...`.

The function `fibonacci_series(n)` returns an empty list when `n` is zero or negative. The function `nth_fibonacci(n)` returns `0` for index `0` and `1` for index `1`.

**Potential limitations**

- The main program does not reject negative term counts; it prints an empty list and skips the final-term calculation.
- Large requested values may produce large integers and require additional computation.
- The function annotations do not enforce integer inputs at runtime.

**Recommendations**

- Add tests for zero, one, several terms, and negative inputs.
- Clearly document the difference between a term count and a zero-based index.
- Consider validating negative term counts if they should be treated as invalid input.

### 3.3 `structure_to_dict.py`

**Implemented functionality**

- `dataclass_to_dict(obj)` converts a dataclass instance using `dataclasses.asdict()`.
- `object_to_dict(obj)` converts an object's instance attributes using `vars()`.
- `pairs_to_dict(pairs)` converts key-value pairs into a dictionary using `dict()`.
- `records_to_dict(students)` creates a dictionary keyed by student roll number.

The main program demonstrates these conversions using a `Student` dataclass, a `Book` class, key-value pairs, and a list of student records.

**Correctness observations**

The implementation demonstrates the four conversion approaches described in the source-code documentation. The student records contain the student's name, branch, and marks under their roll number.

**Potential limitations**

- If two student records have the same roll number, the later record overwrites the earlier one in the resulting dictionary.
- If key-value pairs contain duplicate keys, the later value replaces the earlier value.
- `object_to_dict()` relies on the object exposing an instance attribute dictionary, as ordinary instances of the provided `Book` class do.
- The conversion functions do not perform additional validation of their arguments.

**Recommendations**

- Add examples or tests for duplicate keys and duplicate roll numbers.
- Document the expected input types for each conversion function.
- Add validation if the functions will be used with untrusted or inconsistent data.

## 4. README Audit

The README was reviewed against the documented source code and the README content prepared for this repository.

| Claim | Status | Code Evidence | Recommendation |
|---|---|---|---|
| The project contains three Python programs demonstrating basic programming concepts. | Supported | The three source files implement factorial, Fibonacci, and dictionary-conversion examples. | Keep the project overview. |
| Factorial is calculated using iterative and recursive methods. | Supported | `factorial_iterative()` uses a loop; `factorial_recursive()` uses recursive calls. | Keep the explanation. |
| Negative factorial inputs raise `ValueError`. | Supported | Both factorial functions check `n < 0` and raise `ValueError`. | Mention that the main program catches this exception. |
| The Fibonacci program generates the first `n` terms. | Supported | `fibonacci_series(n)` appends the first `n` sequence values. | Keep the explanation and clarify that non-positive values return an empty list. |
| `nth_fibonacci()` uses zero-based indexing. | Supported | Its docstring defines `F(0) = 0` and `F(1) = 1`. | Keep the explanation. |
| The Fibonacci main program prints the requested final term. | Supported | It calls `nth_fibonacci(terms - 1)` when `terms > 0`. | Clarify that the displayed index is zero-based. |
| Dataclasses are converted using `asdict()`. | Supported | `dataclass_to_dict(obj)` returns `asdict(obj)`. | Keep the explanation. |
| Ordinary objects are converted using `vars()`. | Supported | `object_to_dict(obj)` returns `dict(vars(obj))`. | Explain that this applies to compatible objects exposing instance attributes. |
| Key-value pairs are converted using `dict()`. | Supported | `pairs_to_dict(pairs)` returns `dict(pairs)`. | Keep the explanation. |
| Student records are stored in a dictionary keyed by roll number. | Supported | `records_to_dict(students)` uses `s.roll_no` as the dictionary key. | Mention that duplicate roll numbers overwrite earlier entries. |
| The programs require Python 3. | Partially Supported | The source uses built-in generic annotations such as `list[int]` and `list[tuple]`. | Specify Python 3.9 or later. |
| The project requires no third-party packages. | Supported | The imports shown use Python standard-library modules, including `dataclasses`. | Keep the statement, assuming no additional dependencies are introduced. |
| The listed execution commands match the source filenames. | Supported | The commands `python factorial.py`, `python fibonacci.py`, and `python structure_to_dict.py` match the filenames. | Keep the commands and mention that `python3` may be used where appropriate. |
| The learning objectives include loops, recursion, lists, dictionaries, classes, dataclasses, and exception handling. | Supported | These concepts appear in the loops, recursive function, collections, class definitions, conversions, and `try`/`except` blocks. | Keep the learning objectives. |
| The programs have been tested successfully. | Not Supported | No test results or execution evidence were provided for this audit. | Do not claim successful testing without evidence. |

## 5. Requirements and Compatibility

### Python version

**Recommended minimum: Python 3.9.**

The source files use built-in collection type annotations such as `list[int]` and `list[tuple]`. These annotations require Python 3.9 or later in the code as written.

### Dependencies

The source code uses standard-library functionality:

- `dataclasses` — for the `Student` dataclass and `asdict()`.
- Built-in functions such as `int()`, `print()`, `input()`, `dict()`, and `vars()`.

No third-party package imports appear in the reviewed source code.

### Execution commands

Run each program from the directory containing the Python files:

```bash
python factorial.py
python fibonacci.py
python structure_to_dict.py
```

On systems where Python 3 is invoked with a separate command, use `python3` instead of `python`.

These commands match the provided filenames, but their successful execution has not been verified as part of this audit.

## 6. Potential Issues and Limitations

The following observations are based on source inspection:

1. **Recursive factorial limitations:** Large inputs may exceed Python's recursion limit.
2. **Fibonacci negative term counts:** `fibonacci_series()` returns an empty list rather than raising an error for negative values.
3. **Duplicate dictionary keys:** Duplicate keys or roll numbers overwrite earlier values.
4. **Runtime input validation:** Type annotations do not automatically validate function arguments.
5. **Testing evidence:** No separate test suite or execution results were provided, so runtime behavior has not been independently verified.
6. **Documentation detail:** The README should specify Python 3.9 or later instead of the broader phrase “Python 3.”

These are a mixture of implementation limitations and possible improvements; they do not all represent confirmed bugs.

## 7. Recommendations

- Update the README requirements to specify Python 3.9 or later.
- Add a `tests/` directory with test cases for normal inputs and edge cases.
- Test factorial calculations for `0`, `1`, positive numbers, and negative numbers.
- Test Fibonacci generation for zero, one, multiple terms, and negative values.
- Test dictionary conversion with duplicate keys and duplicate student roll numbers.
- Document the expected argument types and behavior of each function.
- Keep `README.md` focused on setup, usage, and learning objectives.
- Keep `AUDIT.md` focused on code-review findings, limitations, and recommendations.
- Update this report whenever the source code or README changes.

## 8. Final Audit Summary

Based on source inspection, the three Python files implement the functionality described in the README: factorial calculation, Fibonacci sequence operations, and several approaches to converting structured data into dictionaries.

The main documentation improvement is to specify **Python 3.9 or later**. Other useful improvements include explaining negative Fibonacci term counts, duplicate dictionary keys, and the limitations of recursive factorial calculation.

No unsupported claim of successful testing should be included without actual test evidence.

This report records a source-code and documentation review. It does not certify that the programs have been executed or passed a test suite.
