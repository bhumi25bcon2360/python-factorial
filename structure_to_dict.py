"""Structure-to-Dictionary conversion.

Shows three common ways to turn a structured Python object into a dictionary:
1. A @dataclass  -> dict using dataclasses.asdict()
2. A normal class -> dict using vars() / __dict__
3. A list of (key, value) tuples -> dict using dict()
Also converts a list of student records into a dictionary keyed by roll number.
"""
from dataclasses import dataclass, asdict


@dataclass
class Student:
    roll_no: str
    name: str
    branch: str
    marks: int


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


def dataclass_to_dict(obj) -> dict:
    return asdict(obj)


def object_to_dict(obj) -> dict:
    return dict(vars(obj))


def pairs_to_dict(pairs: list[tuple]) -> dict:
    return dict(pairs)


def records_to_dict(students: list[Student]) -> dict:
    """Map roll_no -> rest of the record."""
    return {s.roll_no: {"name": s.name, "branch": s.branch, "marks": s.marks}
            for s in students}


if __name__ == "__main__":
    s = Student("D001", "BHUMI", "CSE", 88)
    print("Dataclass  ->", dataclass_to_dict(s))

    b = Book("Clean Code", "Robert C. Martin", 2008)
    print("Object     ->", object_to_dict(b))

    print("Pairs      ->", pairs_to_dict([("python", 3), ("java", 2), ("c", 1)]))

    students = [Student("D001", "BHUMI", "CSE", 88),
                Student("S002", "Diya", "ECE", 92)]
    print("Records    ->", records_to_dict(students))
