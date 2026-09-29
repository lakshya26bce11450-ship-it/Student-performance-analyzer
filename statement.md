# Problem Statement

## Problem statement
Teachers and students often calculate total marks, percentage, grade and pass/fail status by hand. This is slow and error-prone, especially when a student must score at least 35 in *every* subject to pass, and when results need to be stored and compared later.

## Scope of the project
- Accepts marks (0-100) for four subjects: Physics, Chemistry, Mathematics, English.
- Validates input and computes total, percentage, grade and PASS/FAIL.
- Saves results to a CSV file and shows a history table with class-level analytics.
- Desktop application (Tkinter), works offline, single user.
- **Out of scope:** user login, multiple classes/semesters, online sync.

## Target users
- School / college teachers evaluating a small class.
- Students who want to check their own result and grade.

## High-level features
1. **Input & Validation module** - checks that every field is a valid number from 0 to 100.
2. **Result Calculation module** - total, percentage, grade (A+ to F) and PASS/FAIL rule.
3. **Reporting & Storage module** - save records to CSV, view history, pass rate, average, topper, clear history.
4. Logging of all actions to `logs/app.log`.
5. Unit tests for all logic modules.
