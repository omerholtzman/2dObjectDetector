import numpy as np
from PIL import Image


def quantize(image: np.ndarray, n_quants: int = 2) -> np.ndarray:
    image = Image.fromarray(image)
    image = image.quantize(n_quants)
    return np.array(image)
