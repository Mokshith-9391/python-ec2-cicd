import unittest
from app import HOST, PORT


class TestApp(unittest.TestCase):

    def test_server_configuration(self):
        self.assertEqual(HOST, "0.0.0.0")
        self.assertEqual(PORT, 8000)


if __name__ == "__main__":
    unittest.main()