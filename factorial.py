"""Factorial of a number - iterative and recursive versions."""


def factorial_iterative(n: int) -> int:
    """Return n! using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Return n! using recursion: n! = n * (n-1)!"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"{num}! (iterative) = {factorial_iterative(num)}")
        print(f"{num}! (recursive) = {factorial_recursive(num)}")
    except ValueError as e:
        print("Error:", e)
