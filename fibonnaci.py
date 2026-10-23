"""Fibonacci series - generate the first n terms."""


def fibonacci_series(n: int) -> list[int]:
    """Return a list with the first n Fibonacci numbers (0, 1, 1, 2, 3, ...)."""
    if n <= 0:
        return []
    series = [0]
    a, b = 0, 1
    for _ in range(n - 1):
        series.append(b)
        a, b = b, a + b
    return series


def nth_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed): F(0)=0, F(1)=1."""
    if n < 0:
        raise ValueError("n must be non-negative.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    try:
        terms = int(input("How many Fibonacci terms? "))
        print("Series:", fibonacci_series(terms))
        if terms > 0:
            print(f"Term #{terms - 1} (0-indexed) = {nth_fibonacci(terms - 1)}")
    except ValueError as e:
        print("Error:", e)
