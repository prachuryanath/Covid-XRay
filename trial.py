import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

def load_model():
  model = tf.keras.models.load_model('model')
  return model

def load_and_prep_image(filename, img_shape=224):
  """
  Reads in an image from filename, turns it into a tensor and reshapes into (224,224,3).
  """
  # Read in the image
  img = tf.io.read_file(filename)
  # Decode it into a tensor
  img = tf.image.decode_jpeg(img, channels=3)
  # Resize the image
  img = tf.image.resize(img, [img_shape, img_shape])
  # Rescale the image (get all values between 0 and 1)
  img = img/255.
  return img

class_names = np.array(['CT_COVID','CT_NonCOVID'])

def pred_and_plot(model, filename, class_names):
  """
  Imports an image located at filename, makes a prediction on it with
  a trained model and plots the image with the predicted class as the title.
  """
  # Import the target image and preprocess it
  img = load_and_prep_image(filename)

  # Make a prediction
  pred = model.predict(tf.expand_dims(img, axis=0))

  # Get the predicted class
  pred_round = int(tf.round(pred))
  if pred_round == 1:
    pred_class = "NonCovid"
  else:
    pred_class = "Covid"

  # Plot the image and predicted class
  plt.imshow(img)
  plt.title(f"Prediction: {pred_class}")
  plt.axis(False);
  return pred, pred_class

model = load_model()
prediction = pred_and_plot(model, "data/CT_COVID/Covid(1028).png", class_names)
print(prediction)
print('byeeeeeeeeeeeee')
