import copy
import itertools

import numpy as np
from edge_detection import *
from utils import COLORS


class ObjectDetector:
    def __init__(self, image):
        self.original_image = image
        self.image = image

    def detect_objects(self):
        # clean noise

        # find edges
        self.image = basic_conv_edge_detection(self.image)

        # classify objects
        self.classify_objects()

    def classify_objects(self):
        """
        Gets a np.array of 1 on edges and 0 on background and gives each unique object a different number.
        :param image: the edges image
        :return: new image with each object given a different number
        """
        # while the np.array has 1s:
        object_classification = 2
        while np.any(self.image == 1):
            # find the first 1:
            object_root = np.where(self.image == 1)
            object_root = (object_root[0][0], object_root[1][0])
            self.color_connected_edges(object_root[0], object_root[1], object_classification)
            object_classification += 1

    def color_connected_edges(self, x, y, object_classification):
        self.image[x, y] = object_classification
        x_options = [x - 1, x, x + 1]
        y_options = [y - 1, y, y + 1]
        for x, y in itertools.product(x_options, y_options):
            if self.image[x, y] == 1:
                self.color_connected_edges(x, y, object_classification)

    def get_colored_image(self):
        image = copy.deepcopy(self.image)
        for value in np.unique(self.image):
            image[image == value] = COLORS[value]
        return image
