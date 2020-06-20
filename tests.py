# Wendy Roberts

import unittest
from check_pwd import func1

class TestCase(unittest.TestCase):

    def setUp(self):
        good_pw = ""

    def test_mydate(self):
        self.assertEqual(None, func1(87))


if __name__ == '__main__':
    unittest.main()
