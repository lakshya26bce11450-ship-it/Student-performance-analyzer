# Student Performance Analyzer

## Overview
A desktop application built with Python and Tkinter that calculates a student's total, percentage, grade and PASS/FAIL result from four subject marks, stores results in a CSV file and shows class-level analytics (pass rate, average, topper).

## Features
- Marks entry for Physics, Chemistry, Mathematics and English
- Input validation (empty, non-numeric, NaN/inf, out of range 0-100)
- Grade calculation: A+ (>=90), A (>=80), B (>=70), C (>=60), D (>=50), E (<50), F (fail)
- Fail rule: scoring below 35 in any single subject = FAIL
- Save student records to `data/results.csv`
- History window with summary: students, passed, pass rate, average %, topper
- Clear history, Clear form
- Activity and error logging to `logs/app.log`

## Technologies / tools used
Python 3.8+, Tkinter (GUI), csv, logging, unittest, Git/GitHub. No external packages.

## Project structure
```
student_performance_analyzer/
├── main.py                  # entry point
├── analyzer/
│   ├── config.py            # constants, grading rules, colours
│   ├── validators.py        # Module 1: input validation
│   ├── calculator.py        # Module 2: result & grade logic
│   ├── history.py           # Module 3: CSV storage & analytics
│   ├── gui.py               # Tkinter interface
│   └── logger_setup.py      # logging
├── tests/                   # unit tests
├── docs/DESIGN.md           # architecture & UML diagrams
├── data/                    # results.csv is created here
├── logs/                    # app.log is created here
├── statement.md
└── README.md
```

## Steps to install & run
```bash
git clone <your-repo-url>
cd student_performance_analyzer
python main.py
```
Tkinter ships with Python on Windows/macOS. On Ubuntu/Debian: `sudo apt install python3-tk`.

## Instructions for testing
```bash
python -m unittest discover -s tests -t .
```
Runs 16 tests covering validators, calculator (all grade boundaries, fail rule) and history storage.

Manual test: enter `95, 92, 91, 90` -> Total 368 / 400, 92.0%, Grade A+, PASS. Enter `100, 100, 100, 34` -> FAIL.

## Non-functional requirements
| Type | Requirement |
|---|---|
| Usability | Simple single-window form; clear error dialogs; Clear button |
| Reliability | All bad input handled without crashing; file errors caught |
| Maintainability | Logic separated from GUI; constants in one config file |
| Error handling | Custom `ValidationError`; `OSError` handling for file I/O |
| Logging | Every calculation, save and error written to `logs/app.log` |
| Performance | Result shown instantly (O(n) on 4 subjects) |

## Screenshots
_Add screenshots of the main window and history window here (`docs/screenshots/`)._

## Author
<Your Name> - <Registration Number> - VITyarthi
