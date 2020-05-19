# Importing needed data and tools for future works.

from keras.datasets import cifar10
from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

y_train_to_one_dot = to_categorical(y_train)
y_test_to_one_dot = to_categorical(y_test)

x_train = x_train / 255
x_test = x_test / 255

# Creating the identification model
model = Sequential()

# Convolution Layer
model.add( Conv2D(32, (5, 5), activation='relu', input_shape=(32,32,3) ) )

# MaxPooling Layer
model.add( MaxPooling2D(pool_size=(2, 2)) )

# Convolution Layer
model.add( Conv2D(32, (5, 5), activation='relu') )

# MaxPooling Layer
model.add( MaxPooling2D(pool_size=(2, 2)) )

# Flatten Layer
model.add( Flatten() )

model.add( Dense(1000, activation='relu') )
model.add( Dense(10, activation='softmax') )

# Model compiling
model.compile( loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'] )

# Train model
hist = model.fit( x_train, y_train_to_one_dot, batch_size=256, epochs=10, validation_split=0.3 )

# Get model accuracy
model.evaluate(x_test, y_test_to_one_dot)[1]

model.save('my_model.h5')
