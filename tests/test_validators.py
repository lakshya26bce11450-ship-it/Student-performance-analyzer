import unittest

from analyzer.validators import ValidationError, parse_marks


class TestValidators(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(parse_marks(["50", "60.5", "0", "100"]), [50.0, 60.5, 0.0, 100.0])

    def test_empty_field(self):
        with self.assertRaises(ValidationError):
            parse_marks(["50", "", "70", "80"])

    def test_text_input(self):
        with self.assertRaises(ValidationError):
            parse_marks(["abc", "60", "70", "80"])

    def test_nan_and_inf_rejected(self):
        for bad in ("nan", "inf", "-inf"):
            with self.assertRaises(ValidationError):
                parse_marks([bad, "60", "70", "80"])

    def test_out_of_range(self):
        for bad in ("-1", "100.5", "101"):
            with self.assertRaises(ValidationError) as ctx:
                parse_marks([bad, "60", "70", "80"])
            self.assertEqual(ctx.exception.title, "Invalid marks")


if __name__ == "__main__":
    unittest.main()
