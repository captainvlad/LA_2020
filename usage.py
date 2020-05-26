from general import router_function

#Example to call each one of subfunctions

# rotate_image
# router_function( "sample_5.jpg", [1, 90] )
# flipper
# router_function( "sample_5.jpg", [2, -1] )
# grayscale_filter
# router_function( "sample_5.jpg", [3] )
# sepia_filter
# router_function( "sample_5.jpg", [4] )
# add_brightness_to_image
# router_function( "sample_5.jpg", [5, 50, 50, 50] )
# negative
# router_function( "sample_5.jpg", [6] )
# contrast
# router_function( "sample_5.jpg", [7, 10] )
# gamma_correction
# router_function( "sample_5.jpg", [8, 5] )
# Gaussian_blur
# router_function( "sample_5.jpg", [9] )
# jpeg_algorithm
# router_function( "sample_5.jpg", [10] )
# svd
# router_function( "sample_5.jpg", [11] )
# get_predictions
router_function( "sample_5.jpg", [12] )