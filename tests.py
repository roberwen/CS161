# Wendy Roberts

import unittest
from check_pwd import func1

class TestCase(unittest.TestCase):

    def setUp(self):
        good_pw = ""

    def test_func1(self):
        self.assertEqual(0, func1("dog"))


if __name__ == '__main__':
    unittest.main()
