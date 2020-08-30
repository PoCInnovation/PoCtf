from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import RMSprop, Adam
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

json_file = open('flag.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("flag.h5")
print("Loaded model from disk")

opt = Adam(learning_rate=0.01)

loaded_model.compile(loss='binary_crossentropy',
            optimizer=opt,
            metrics=['accuracy'])


def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (200, 200, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


image = load(sys.argv[1])
predictions = loaded_model.predict(image)
print(predictions)
image_path = sys.argv[1]
img = mpimg.imread(image_path)
plt.imshow(img)
if predictions[0][0] > 0.5:
    plt.title("%.2f" % (predictions[0][0]*100) + "% other" + image_path)
else:
    plt.title("%.2f" % ((1-predictions[0][0])*100) + "% flag"+ image_path)
plt.show()
