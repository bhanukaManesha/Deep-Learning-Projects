

from keras.models import load_model

new_model = load_model("cat_dogs_net.h5")


new_model.summary()

new_model.get_weights()

new_model.optimizer
