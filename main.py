import utils
from IO import read_image, GRAYSCALE
from object_detector import ObjectDetector
import matplotlib.pyplot as plt
import numpy as np


FILE_PATH = ""

if __name__ == '__main__':
    image = utils.get_two_squares_image()[0]
    found_objects = ObjectDetector(image)
    found_objects.detect_objects()
    colored_image = found_objects.get_colored_image()
    print(np.unique(colored_image))
    # show the colored image:
    plt.imshow(colored_image)
    plt.show()
