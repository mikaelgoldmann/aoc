import unittest
from dec23 import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual("92658374", main("389125467", 10))
        self.assertEqual("67384529", main("389125467", 100))
        self.assertEqual("98752463", main("789465123", 100))
