import utils

from edge_detection import *


def test_basic_conv_edge_detection():
    image, square_side_size = utils.get_square_image()
    derivative_image = basic_conv_edge_detection(image)
    duplicate_side_edge = 1
    expected_edge_numbers = 4 * (2 * square_side_size - duplicate_side_edge)
    assert(np.sum(derivative_image) == expected_edge_numbers)

