import numpy as np
from PIL import Image

MAX_POINT_VALUE = 256


def quantize(image: np.ndarray, n_quants: int = 2) -> np.ndarray:
    image = Image.fromarray(image * MAX_POINT_VALUE).convert('L')
    image = image.quantize(n_quants)
    return 1 - np.array(image)
