import unittest
from dec23 import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main("389125467", 10), "92658374")
        self.assertEqual(main("389125467", 100), "67384529")
        self.assertEqual(main("789465123", 100), "98752463")
