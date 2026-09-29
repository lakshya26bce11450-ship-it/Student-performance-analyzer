import tempfile
import unittest
from pathlib import Path

from analyzer import history
from analyzer.calculator import calculate_result


class TestHistory(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "results.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def _save(self, name, marks):
        history.save_record(name, marks, calculate_result(marks), self.path)

    def test_load_missing_file(self):
        self.assertEqual(history.load_records(self.path), [])

    def test_save_and_load(self):
        self._save("Asha", [90, 90, 90, 90])
        self._save("Ravi", [80, 20, 80, 80])
        rows = history.load_records(self.path)
        self.assertEqual([r["name"] for r in rows], ["Asha", "Ravi"])
        self.assertEqual(rows[1]["result"], "FAIL")

    def test_summary(self):
        self._save("Asha", [90, 90, 90, 90])
        self._save("Ravi", [80, 20, 80, 80])
        s = history.summarize(history.load_records(self.path))
        self.assertEqual((s["count"], s["passed"], s["pass_rate"], s["topper"]),
                         (2, 1, 50.0, "Asha"))

    def test_summary_empty(self):
        self.assertEqual(history.summarize([])["count"], 0)

    def test_clear(self):
        self._save("Asha", [90, 90, 90, 90])
        history.clear_history(self.path)
        self.assertEqual(history.load_records(self.path), [])


if __name__ == "__main__":
    unittest.main()
