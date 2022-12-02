import numpy as np
from PIL import Image
import random

MAX_POINT_VALUE = 256
COLORS = [0] + [random.randint(0, 256) for _ in range(20)]


def quantize(image: np.ndarray, n_quants: int = 2) -> np.ndarray:
    image = Image.fromarray(image * MAX_POINT_VALUE).convert('L')
    image = image.quantize(n_quants)
    return 1 - np.array(image)


def get_square_image():
    picture_size = 100
    image = np.zeros((picture_size, picture_size))
    # add a square in the middle with edge size = 20:
    square_edge_size = 20
    image[picture_size // 2 - square_edge_size // 2:picture_size // 2 + square_edge_size // 2,
          picture_size // 2 - square_edge_size // 2:picture_size // 2 + square_edge_size // 2] = 1
    return image, square_edge_size


def get_two_squares_image():
    picture_size = 100
    image = np.zeros((picture_size, picture_size))
    # add a square in the middle with edge size = 20:
    square_edge_size = 20
    image[picture_size // 2 - square_edge_size // 2 - 30 :picture_size // 2 + square_edge_size // 2 - 30,
          picture_size // 2 - square_edge_size // 2 - 10:picture_size // 2 + square_edge_size // 2] = 1
    image[picture_size // 2 - square_edge_size // 2:picture_size // 2 + square_edge_size // 2,
          picture_size // 2 + square_edge_size // 2:picture_size // 2 + 3 * square_edge_size // 2] = 1
    return image, square_edge_size
