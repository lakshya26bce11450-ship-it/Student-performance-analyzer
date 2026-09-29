"""Central configuration: constants, grading rules and the GUI colour theme."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "results.csv"
LOG_FILE = BASE_DIR / "logs" / "app.log"

APP_TITLE = "Student Performance Analyzer"
SUBJECTS = ["Physics", "Chemistry", "Mathematics", "English"]
MAX_MARK = 100          # maximum marks per subject
MIN_MARK = 0
PASS_MARK = 35          # a student fails if any subject is below this

# (minimum percentage, grade) - checked from highest to lowest.
GRADE_BANDS = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")]
LOWEST_PASS_GRADE = "E"
FAIL_GRADE = "F"

# Color theme for the app
APP_BG = "#EAF2FF"
TITLE_BG = "#19376D"
TITLE_FG = "#FFFFFF"
TEXT_COLOR = "#102A43"
INPUT_BG = "#FFFFFF"
PRIMARY_BUTTON = "#2563EB"
SECONDARY_BUTTON = "#64748B"
RESULT_BG = "#DBEAFE"
RESULT_FG = "#1E3A8A"
