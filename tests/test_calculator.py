import unittest

from analyzer.calculator import calculate_grade, calculate_result, format_result


class TestCalculator(unittest.TestCase):
    def test_grade_boundaries(self):
        cases = {90: "A+", 89.99: "A", 80: "A", 70: "B", 60: "C", 50: "D", 49.99: "E"}
        for pct, grade in cases.items():
            self.assertEqual(calculate_grade(pct), grade, pct)

    def test_pass_all_subjects(self):
        r = calculate_result([95, 92, 91, 90])
        self.assertEqual((r.total, r.percentage, r.grade, r.result), (368, 92.0, "A+", "PASS"))

    def test_fail_when_one_subject_below_35(self):
        r = calculate_result([100, 100, 100, 34])
        self.assertEqual((r.grade, r.result), ("F", "FAIL"))

    def test_exactly_35_passes(self):
        r = calculate_result([35, 35, 35, 35])
        self.assertEqual((r.result, r.grade), ("PASS", "E"))

    def test_all_zero_fails(self):
        self.assertEqual(calculate_result([0, 0, 0, 0]).result, "FAIL")

    def test_format_result(self):
        text = format_result(calculate_result([80, 80, 80, 80]))
        self.assertIn("Total: 320 / 400", text)
        self.assertIn("Percentage: 80.0%", text)
        self.assertIn("Grade: A", text)
        self.assertIn("Result: PASS", text)


if __name__ == "__main__":
    unittest.main()
