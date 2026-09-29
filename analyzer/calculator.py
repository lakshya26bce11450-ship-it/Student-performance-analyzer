"""Module 2 - Result calculation & grading (pure logic, no GUI)."""
from dataclasses import dataclass

from analyzer import config


@dataclass(frozen=True)
class Result:
    total: float
    percentage: float
    grade: str
    result: str          # "PASS" or "FAIL"


def calculate_grade(percentage):
    """Map a percentage to a grade for a passing student."""
    for minimum, grade in config.GRADE_BANDS:
        if percentage >= minimum:
            return grade
    return config.LOWEST_PASS_GRADE


def calculate_result(marks):
    """Compute total, percentage, grade and PASS/FAIL from a list of marks."""
    total = sum(marks)
    percentage = total / len(marks)

    # A student fails if they score less than 35 in any one subject.
    if min(marks) < config.PASS_MARK:
        return Result(total, percentage, config.FAIL_GRADE, "FAIL")
    return Result(total, percentage, calculate_grade(percentage), "PASS")


def format_result(res):
    """Text shown in the result box of the GUI."""
    max_total = config.MAX_MARK * len(config.SUBJECTS)
    return ("Total: " + str(res.total) + " / " + str(max_total) + "\n"
            "Percentage: " + str(round(res.percentage, 2)) + "%\n"
            "Grade: " + res.grade + "\n"
            "Result: " + res.result)
