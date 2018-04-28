# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os,random, sys

classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Flatten())
#classifier.add(Dense(units = 128, activation = 'relu'))
#classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.add(Dense(8, input_dim=4, activation='relu'))
classifier.add(Dense(18, activation='softmax'))
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
train = 'type1_sorted/train'
test = 'type1_sorted/test'
training_set = train_datagen.flow_from_directory(train, target_size = (64, 64), batch_size = 32, class_mode = 'categorical')
test_set = test_datagen.flow_from_directory(test, target_size = (64, 64), batch_size = 32, class_mode = 'categorical')

classifier.fit_generator(training_set, steps_per_epoch = 752, epochs = 25, 
                         validation_data = test_set, validation_steps = 188)

path = 'type1_sorted/test/Normal'
a = random.choice(os.listdir(path))
test_image = image.load_img(path+'/'+a, target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
print(result[0][0])