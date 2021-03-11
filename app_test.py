"""Unit test file for app.py"""
from app import returnBackwardsString
import unittest
class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""
    def test_return_backwards_string(self):
        """Test return backwards simple string"""
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, returnBackwardsString(random_string))
if __name__ == "__main__":
    unittest.main()
