from keras.models import load_model
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np


def get_predictions(imagename):

    model = load_model('my_model.h5')
    my_image = plt.imread(imagename)

    my_image = resize( my_image, (32,32,3) )
    probabilities = model.predict( np.array( [my_image] ) )

    labels_order = [ ['airplane'], ['automobile'], ['bird'], ['cat'], ['deer'], ['dog'], ['frog'],
                     ['horse'], ['ship'], ['truck'] ]

    for i in range( len(labels_order) ):
        labels_order[i].append( round(probabilities[0][i] * 100, 2) )

    labels_order.sort(key=lambda x: x[1], reverse=True)
    return labels_order

# print( get_predictions("sample_5.jpg") )