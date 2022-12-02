import numpy as np
from edge_detection import *

class ObjectDetector:
    def __init__(self, image):
        self.image = image


    def detect_objects(self):
        # clean noise

        # find edges
        edges = basic_edge_detection(self.image)



    @staticmethod
    def classify_objects(image: np.ndarray) -> np.ndarray:
        """
        Gets a np.array of 1 on edges and 0 on background and gives each unique object a different number.
        :param image: the edges image
        :return: new image with each object given a different number
        """
        # while the np.array has 1s:
        object_classification = 2
        while np.any(image == 1):
            # find the first 1:
            object_root = np.where(image == 1)
            object_root = (object_root[0][0], object_root[1][0])

            # find all the 1s connected to it:

