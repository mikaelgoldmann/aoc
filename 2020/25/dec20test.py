import unittest
import dec25


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(11, dec25.loop_size(17807724))
        self.assertEqual(8, dec25.loop_size(5764801))