
# Getting the user input for the image path
image_path = input("Please enter the image path : ")

#  Loading the nympy library
import numpy as np

# From keras,models load the load model method
from keras.models import load_model

# Loading the model
new_model = load_model("cat_dogs_net.h5")

# Printing out the summary of the model
new_model.summary()

# Getting the image methods from keras
from keras.preporocessing import image

test_image = image.load(image_path, target_size = (64,64))


test_image = image.img_to_array(test_image)

test_image = np.expand_dims(test_image, axis = 0)

result = new_model.predict(test_image)

new_model.class_indicies

if result[0][1]:
	prediction = "dog"
	print("It is a beautiful dog !!")
else:
	prediction = "cat"
	print("It is a cute cat !! ")


print("\nThank You for using the cat_dogs_net | Bhanuka Gamage")


