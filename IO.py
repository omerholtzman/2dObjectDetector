
import numpy as np
from skimage import io

GRAYSCALE = 1
RGB = 2
MAX_POINT_VALUE = 256
RGB_TO_GREYSCALE = [0.299, 0.587, 0.114]

FILE_NOT_FOUND_ERROR = "Error: file not found"
VALUE_VALIDITY_ERROR_MESSAGE = "Error: representation value is not valid"


def read_image(filename, representation):
    """
    Reads an image and converts it into a given representation
    :param filename: filename of image on disk
    :param representation: 1 for greyscale and 2 for RGB
    :return: Returns the image as an np.float64 matrix normalized to [0,1]
    """
    # Read the image
    try:
        image = io.imread(filename)
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        return

    if representation != GRAYSCALE and representation != RGB:
        raise ValueError(VALUE_VALIDITY_ERROR_MESSAGE)

    if representation == GRAYSCALE:
        # Convert to grayscale
        image = image.astype(np.float64)
        image = np.dot(image[..., :3], RGB_TO_GREYSCALE)
    # return the image normalized to [0,1]
    return image / MAX_POINT_VALUE


def save_image(image: np.ndarray, path: str):
    """
    Saves an image to the given path
    :param image: The image to save
    :param path: The path to save the image to
    """
    io.imsave(path, image)
