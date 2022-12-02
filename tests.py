import unittest

from edge_detection import *


class EdgeDetectionTests(unittest.TestCase):
    def test_basic_conv_edge_detection(self):
        picture_size = 100
        image = np.zeros((picture_size, picture_size))
        # add a square in the middle with edge size = 20:
        square_edge_size = 20
        image[picture_size // 2 - square_edge_size // 2:picture_size // 2 + square_edge_size // 2,
              picture_size // 2 - square_edge_size // 2:picture_size // 2 + square_edge_size // 2] = 1

        derivative_image = basic_conv_edge_detection(image)
        duplicate_side_edge = 1
        expected_edge_numbers = 4 * (2 * square_edge_size - duplicate_side_edge)
        self.assertEqual(np.sum(derivative_image), expected_edge_numbers)


if __name__ == '__main__':
    unittest.main()
