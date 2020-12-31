import unittest
import dec20


class Dec20Test(unittest.TestCase):
    def testRotate0DoesCopy(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = dec20.rot_left(a, 0)
        self.assertEqual([[1, 2, 3], [4, 5, 6]], a)
        self.assertEqual([[1, 2, 3], [4, 5, 6]], b)
        self.assertNotEqual(id(a), id(b))
        for r, s in zip(a, b):
            self.assertNotEqual(id(r), id(s))

    def test_rotate(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = dec20.rot_left(a)
        self.assertEqual([[1, 2, 3], [4, 5, 6]], a)
        self.assertEqual([[3, 6], [2, 5], [1, 4]], b)

    def test_rotate2(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = dec20.rot_left(a, times=2)
        self.assertEqual([[1, 2, 3], [4, 5, 6]], a)
        self.assertEqual([[6, 5, 4], [3, 2, 1]], b)

    def test_flip(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        b = dec20.flip_top_bottom(a)
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], a)
        self.assertEqual([[10, 11, 12], [7, 8, 9], [4, 5, 6], [1, 2, 3]], b)

    def test_orientations(self):
        # Note! This test the rotations and reflections. It does not
        # test the left / top / bottom / right settings as those only
        # work as expected when the matrix entries are '.' and '#'
        a = [[1,2], [3, 4]]
        expected = [
            dec20.Orientation([[1, 2], [3, 4]]),
            dec20.Orientation([[2, 4], [1, 3]]),
            dec20.Orientation([[4, 3], [2, 1]]),
            dec20.Orientation([[3, 1], [4, 2]]),
            dec20.Orientation([[3, 4], [1, 2]]),
            dec20.Orientation([[1, 3], [2, 4]]),
            dec20.Orientation([[2, 1], [4, 3]]),
            dec20.Orientation([[4, 2], [3, 1]])
        ]
        self.assertEqual(expected, dec20.orientations(a))

    def test_fits(self):
        grid = [[None, None], [None, None]]
        grid[0][0] = 0, dec20.Orientation([['.', '.'], ['#', '#']])
        piece1 = dec20.Orientation([['.', '#'],['#', '.']])
        piece2 = dec20.Orientation([['#', '#'], ['.', '.']])
        self.assertTrue(dec20.fits(piece1, grid, 0, 1))
        self.assertFalse(dec20.fits(piece1, grid, 1, 0))
        self.assertFalse(dec20.fits(piece2, grid, 0, 1))
        self.assertTrue(dec20.fits(piece2, grid, 1, 0))

    def test_trim_tile(self):
        tile = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(dec20.trim_tile(tile), [[6, 7], [10, 11]])
        self.assertEqual(tile, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    def test_flatten(self):
        tile0 = [[0, 0], [0, 0]]
        tile1 = [[1, 1], [1, 1]]
        tile2 = [[2, 2], [2, 2]]
        tile3 = [[3, 3], [3, 3]]
        grid = [[tile0, tile1], [tile2, tile3]]
        self.assertEqual(dec20.flatten(grid), [[0, 0, 1, 1], [0, 0, 1, 1], [2, 2, 3, 3], [2, 2, 3, 3]])

    def test_monster(self):
        for row in dec20.get_monster():
            print(row)


if __name__ == '__main__':
    unittest.main()
