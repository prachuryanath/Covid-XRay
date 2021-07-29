import keras
from PIL import Image, ImageOps
import numpy as np
from tensorflow.python.keras.backend import dtype


def image_classification(img, model):
    # Load the model
    model = keras.models.load_model('model')

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image = np.asarray(image, dtype=np.float16)
    image_array = image[:,:,:3]
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float16) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    
    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability
