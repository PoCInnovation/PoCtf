from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
from skimage import transform
import sys

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

json_file = open('cat_vs_dogs.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("cats_vs_dogs.h5")
print("Loaded model from disk")

loaded_model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.0001), metrics=['accuracy'])

def load(img):
        np_image = Image.open(img)
        real_image = Image.open("800.jpg")

        pixels1 = np_image.getdata()
        pixels2 = real_image.getdata()
        counter = 0
        if len(pixels1) != len(pixels2):
            return ["not same picture"]
        for i in range(len(pixels1)):
            if pixels1[i] != pixels2[i]:
                counter += 1
        if counter > 15:
            return ["not original"] 
        np_image = np.array(np_image).astype('float32') / 255
        np_image = transform.resize(np_image, (200, 200, 3))
        np_image = np.expand_dims(np_image, axis=0)

        return np_image

image = load(sys.argv[1])
if (image[0] == "not same picture"):
    print("Nope, this isnt a good image, please check size and format")
if (image[0] == "not original"):
    print("Nope, this is not my dog at all")
predictions = loaded_model.predict(image)
print(predictions)
image_path = sys.argv[1]
img = mpimg.imread(image_path)
plt.imshow(img)
if predictions[0][0] > 0.5:
    plt.title("%.2f" % (predictions[0][0]*100) + "% dog " + image_path)
else:
    plt.title("%.2f" % ((1-predictions[0][0])*100) + "% cat " + image_path)
plt.show()
