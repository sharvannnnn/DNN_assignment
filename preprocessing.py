
import tensorflow as tf
import numpy as np

def prepare_image(path):
    img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    return np.expand_dims(img, axis=0)
