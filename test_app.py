import unittest

from app import get_message


class TestApp(unittest.TestCase):

    def test_get_message(self):
        message = get_message()

        self.assertIn("Mokshith", message)
        self.assertIn("GitHub Actions", message)


if __name__ == "__main__":
    unittest.main()