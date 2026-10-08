
from typing import List, Union


class Student:

    def __init__(self, student_id: str, name: str) -> None:
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Error: Student ID must be a non-empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Error: Student name must be a non-empty string.")

        self.student_id: str = student_id.strip()
        self.name: str = name.strip()
        self.grades: List[float] = []

    def add_grade(self, grade: Union[int, float]) -> bool:
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print(f"[{self.name}] Error: Grade '{grade}' must be a numeric value.")
            return False

        if not 0 <= grade <= 100:
            print(
                f"[{self.name}] Error: Grade {grade} is out of range (must be 0-100)."
            )
            return False

        self.grades.append(float(grade))
        print(f"[{self.name}] Successfully added grade: {grade}")
        return True

    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def is_passed(self) -> bool:
        return self.calculate_average() >= 60.0

    def is_honor_roll(self) -> bool:
        return self.calculate_average() >= 90.0

    def remove_grade_by_index(self, index: int) -> bool:
        if not isinstance(index, int) or isinstance(index, bool):
            print(f"[{self.name}] Error: Index '{index}' must be an integer.")
            return False

        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"[{self.name}] Removed grade {removed} at index {index}.")
            return True

        print(
            f"[{self.name}] Error: Index {index} is out of bounds for {len(self.grades)} grades."
        )
        return False

    def remove_grade_by_value(self, value: Union[int, float]) -> bool:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            print(f"[{self.name}] Error: Value '{value}' must be numeric.")
            return False

        val_float = float(value)
        if val_float in self.grades:
            self.grades.remove(val_float)
            print(f"[{self.name}] Removed grade value {val_float}.")
            return True

        print(f"[{self.name}] Error: Grade value {val_float} not found.")
        return False

    def generate_report(self) -> str:
        avg = self.calculate_average()
        letter = self.get_letter_grade()
        status = "Passed" if self.is_passed() else "Failed"
        honor = "Yes" if self.is_honor_roll() else "No"

        report = (
            "========================================\n"
            "        STUDENT SUMMARY REPORT          \n"
            "========================================\n"
            f"Student ID       : {self.student_id}\n"
            f"Student Name     : {self.name}\n"
            f"Number of Grades : {len(self.grades)}\n"
            f"Average Grade    : {avg:.2f}\n"
            f"Letter Grade     : {letter}\n"
            f"Pass/Fail Status : {status}\n"
            f"Honor Roll Status: {honor}\n"
            "========================================"
        )
        print(report)
        return report


def main() -> None:
    print("--- DEMO 1: Creating Student Records ---")
    try:
        student1 = Student("20261001", "Valeria Gutiérrez")
        student2 = Student("20261002", "Alex Miller")
    except ValueError as err:
        print(err)
        return

    print("\n--- DEMO 2: Invalid Initialization (Validation Guard) ---")
    try:
        Student("", "Invalid Student")
    except ValueError as err:
        print(f"Handled validation error: {err}")

    print("\n--- DEMO 3: Adding Valid & Invalid Grades ---")
    student1.add_grade(95.0)
    student1.add_grade(92.5)
    student1.add_grade(88.0)

    # Handled invalid inputs (no crashes)
    student1.add_grade("Fifty")  # Non-numeric
    student1.add_grade(150)      # Out of range
    student1.add_grade(-10)      # Out of range

    student2.add_grade(55.0)
    student2.add_grade(62.0)

    print("\n--- DEMO 4: Removing Grades (By Index and Value) ---")
    student1.remove_grade_by_index(1)      # Removes 92.5
    student1.remove_grade_by_index(99)     # Out of bounds handled gracefully
    student1.remove_grade_by_value(88.0)   # Removes 88.0
    student1.remove_grade_by_value(100.0)  # Value not found handled gracefully

    # Re-adding grades for calculation
    student1.add_grade(95.0)
    student1.add_grade(92.0)

    print("\n--- DEMO 5: Generating Summary Reports ---")
    student1.generate_report()
    print()
    student2.generate_report()


if __name__ == "__main__":
    main()