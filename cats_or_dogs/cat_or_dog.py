from keras.models import load_model
import numpy
from skimage.io import imread
from skimage.transform import resize
import sys

params = sys.argv
image_path = params[1]

print("Testing with poorly trained model.")
model_bad = load_model('cnn_image_classifier.h5')

test_image = imread(image_path)
test_image = resize(test_image, (150, 150, 3))

y_pred = model_bad.predict(numpy.array([test_image]))[0][0]

# "Confidence here is a measure of how close the predicted value is to the maximum it could be in either classification
# A confidence of 1 for dog means y_pred = 1
# A confidence of 1 for cat means y_pred = 0
if y_pred > 0.5:
    print("This is a dog! Maybe, with confidence", y_pred)
else:
    print("This is a cat!!! Possibly, with confidence", 1 - y_pred)

