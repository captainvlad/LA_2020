from affine_transformation import rotate_image, flipper
from color_manipulation import grayscale_filter, sepia_filter,\
    add_brightness_to_image, negative, contrast, gamma_correction, Gaussian_blur
from jpeg_realization import jpeg_algorithm
from svd_example import svd
from tensor_2 import get_predictions


def router_function( imagename, arguments ):

    if arguments[0] == 1 and len(arguments) == 2:
        rotate_image(imagename, arguments[1] )

    elif arguments[0] == 2 and len(arguments) == 2:
        flipper(imagename, arguments[1] )

    elif arguments[0] == 3 and len(arguments) == 1:
        grayscale_filter(imagename)

    elif arguments[0] == 4 and len(arguments) == 1:
        sepia_filter(imagename)

    elif arguments[0] == 5 and len(arguments) == 4:
        add_brightness_to_image(imagename, arguments[0], arguments[1], arguments[2])

    elif arguments[0] == 6 and len(arguments) == 1:
        negative(imagename)

    elif arguments[0] == 7 and len(arguments) == 2:
        contrast(imagename, arguments[1])

    elif arguments[0] == 8 and len(arguments) == 2:
        gamma_correction(imagename, arguments[1])

    elif arguments[0] == 9 and len(arguments) == 1:
        Gaussian_blur(imagename)

    elif arguments[0] == 10 and len(arguments) == 1:
        jpeg_algorithm(imagename)

    elif arguments[0] == 11 and len(arguments) == 1:
        svd(imagename)

    elif arguments[0] == 12 and len(arguments) == 1:
        res = get_predictions(imagename)
        print("Results of recognition are following: \n")
        for item in res:
            print(f"{item[0]} - {item[1]}%")

    else:
        print("Function not found")
        return 1

    print("\nDone")
    return 0