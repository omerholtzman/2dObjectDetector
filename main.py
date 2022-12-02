from IO import read_image, GRAYSCALE
from object_detector import ObjectDetector

FILE_PATH = ""

if __name__ == '__main__':
    image = read_image(FILE_PATH, GRAYSCALE)
    found_objects = ObjectDetector().detect_objects(image)

