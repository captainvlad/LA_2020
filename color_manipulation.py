import cv2
import numpy as np
from  math import pi, e, sqrt

def image_splitter(imagename):
    img = cv2.imread(imagename)
    return  cv2.split(img)

def image_merger( r, g, b ):
    transformed_image = cv2.merge([r, g, b])
    return transformed_image


def change(imagename, matrix):
    r, g, b = image_splitter(imagename)

    r = r * matrix.item(0,0) + g * matrix.item(0,1) + b * matrix.item(0,2)
    g = r * matrix.item(1,0) + g * matrix.item(1,1) + b * matrix.item(1,2)
    b = r * matrix.item(2,0) + g * matrix.item(2,1) + b * matrix.item(2,2)

    return image_merger(r, g, b)

def grayscale_filter(imagename):
    matrix = np.array( [ [1/3 for i in range(3) ] for i in range(3) ] )
    cv2.imwrite( "changed_image.png", change(imagename, matrix) )

def sepia_filter(imagename):
    matrix = np.array([[0.393, 0.769, 0.189],
                        [0.349, 0.686, 0.168],
                        [0.272, 0.534, 0.131]])
    cv2.imwrite( "changed_image.png", change(imagename, matrix) )

def add_brightness_to_image( imagename, value_1 = 0, value_2 = 0, value_3 = 0 ):
    for item in [ value_1, value_2, value_3 ]:
        if item < -150 or item > 150:
            print("All values have to be in [-150, 150] interval!")
            return -1

    r, g, b = image_splitter(imagename)

    r += value_3
    g += value_2
    b += value_1

    cv2.imwrite( "changed_image.png", image_merger(r, g, b) )

def negative( imagename ):
    r, g, b = image_splitter(imagename)

    r = -1 * r + 255
    g = -1 * g + 255
    b = -1 * b + 255

    cv2.imwrite( "changed_image.png", image_merger(r, g, b) )

def contrast( imagename, contrast_grade ):
    r, g, b = image_splitter(imagename)
    f = (259 * (contrast_grade + 255)) / (255 * (259 - contrast_grade))

    r = r * f
    g = g * f
    b = b * f

    cv2.imwrite( "changed_image.png", image_merger(r, g, b) )

def gamma_correction( imagename, f ):
    r, g, b = image_splitter(imagename)

    r = r / f
    g = g / f
    b = b / f

    cv2.imwrite("changed_image.png", image_merger(r, g, b))

def Gaussian_blur( imagename ):
    r, g, b = image_splitter(imagename)

    r = cv2.GaussianBlur(r, (0, 0), cv2.BORDER_DEFAULT )
    g = cv2.GaussianBlur(g, (0, 0), cv2.BORDER_DEFAULT )
    b = cv2.GaussianBlur(b, (0, 0), cv2.BORDER_DEFAULT )

    cv2.imwrite("changed_image.png", image_merger(r, g, b))

# Gaussian_blur("sample_5.jpg", 2)