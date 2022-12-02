
import numpy as np
from scipy import signal
from utils import quantize


def basic_conv_edge_detection(image: np.ndarray) -> np.ndarray:
    der_vec = [[0, 0, 0], [-0.5, 0, 0.5], [0, 0, 0]]  # derivative vector
    x_der = signal.convolve2d(image, der_vec, mode='same')
    y_der = signal.convolve2d(image.T, der_vec, mode='same').T
    magnitude = np.sqrt(np.power(x_der, 2) + np.power(y_der, 2))  # get the magnitude
    return quantize(magnitude)
