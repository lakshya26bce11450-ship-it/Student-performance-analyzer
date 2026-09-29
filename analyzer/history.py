"""Module 3 - Reporting & storage (CSV based create / read / delete)."""
import csv
from datetime import datetime

from analyzer import config

FIELDS = (["timestamp", "name"] + config.SUBJECTS
          + ["total", "percentage", "grade", "result"])


def save_record(name, marks, res, path=None):
    """Append one student's result to the CSV file."""
    path = path or config.DATA_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not path.exists() or path.stat().st_size == 0
    row = {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
           "name": name, "total": res.total,
           "percentage": round(res.percentage, 2),
           "grade": res.grade, "result": res.result}
    row.update(dict(zip(config.SUBJECTS, marks)))
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def load_records(path=None):
    """Return all saved records as a list of dicts (empty if no file)."""
    path = path or config.DATA_FILE
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def clear_history(path=None):
    """Delete all saved records."""
    path = path or config.DATA_FILE
    if path.exists():
        path.unlink()


def summarize(records):
    """Class-level analytics: count, pass rate, average % and topper."""
    if not records:
        return {"count": 0, "passed": 0, "pass_rate": 0.0,
                "average": 0.0, "topper": None}
    passed = sum(1 for r in records if r["result"] == "PASS")
    average = sum(float(r["percentage"]) for r in records) / len(records)
    topper = max(records, key=lambda r: float(r["percentage"]))
    return {"count": len(records), "passed": passed,
            "pass_rate": round(100 * passed / len(records), 2),
            "average": round(average, 2), "topper": topper["name"]}
