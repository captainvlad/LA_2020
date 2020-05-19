import cv2

def rotate_image( imagename, angle ):

    img = cv2.imread(imagename, 1)
    rows, cols, ht = img.shape

    matrix = cv2.getRotationMatrix2D( (rows/2, cols/2), angle, 1 )
    new_image = cv2.warpAffine( img, matrix, (rows, cols) )

    cv2.imwrite(f"{imagename}_rotated.jpg", new_image)

def flipper( imagename, code ):

    if code not in [-1, 0, 1]:
        return -1

    img = cv2.imread(imagename)
    img_2 = cv2.flip(img, code)
    cv2.imwrite("changed_image.png", img_2)


# flipper( "sample_5.jpg", 0 )