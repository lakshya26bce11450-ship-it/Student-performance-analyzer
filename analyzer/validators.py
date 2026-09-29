"""Module 1 - Input & validation."""
import math

from analyzer import config


class ValidationError(Exception):
    """Raised for bad user input. Carries a dialog title and a message."""

    def __init__(self, title, message):
        super().__init__(message)
        self.title = title
        self.message = message


def parse_marks(raw_values):
    """Convert the raw text from the entry boxes into a list of floats.

    Raises ValidationError if a value is not a number, or if any mark is
    outside the range 0 - 100.
    """
    marks = []
    for raw in raw_values:
        try:
            value = float(raw)
        except (TypeError, ValueError):
            raise ValidationError("Invalid input",
                                  "Please enter numbers in all subject boxes.")
        if not math.isfinite(value):          # rejects 'nan' and 'inf'
            raise ValidationError("Invalid input",
                                  "Please enter numbers in all subject boxes.")
        marks.append(value)

    # Every subject mark must be between 0 - 100.
    for mark in marks:
        if mark < config.MIN_MARK or mark > config.MAX_MARK:
            raise ValidationError("Invalid marks",
                                  "Please enter marks from 0 to 100.")
    return marks
