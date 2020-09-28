from app import app
import flask
from flask import make_response, jsonify, request, abort
from flask_cors import CORS
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import RMSprop
import numpy as np
from PIL import Image
from skimage import transform
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession



CORS(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
@app.route('/index')
def index():
    return "Hello PoC!"


@app.route('/api/uploadfile', methods=['POST'])
def test_image():
    data = flask.request.files["myFile"]

    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)

    json_file = open('./cat_vs_dogs.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("./cats_vs_dogs.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.0001), metrics=['accuracy'])

    def load():
        np_image = Image.open(data)
        real_image = Image.open("800.jpg")

        pixels1 = np_image.getdata()
        pixels2 = real_image.getdata()
        counter = 0
        if len(pixels1) != len(pixels2):
            return ["not same picture"]
        for i in range(len(pixels1)):
            if pixels1[i] != pixels2[i]:
                counter += 1
        if counter > 20:
            return ["not original"] 
        np_image = np.array(np_image).astype('float32') / 255
        np_image = transform.resize(np_image, (200, 200, 3))
        np_image = np.expand_dims(np_image, axis=0)

        return np_image

    image = load()
    if (image[0] == "not same picture"):
        return make_response(jsonify({'NOPE': "Nope, this isnt a good image, please check size and format"}), 200)
    if (image[0] == "not original"):
        return make_response(jsonify({'NOPE': "Nope, this is not my dog at all"}), 200)
    predictions = loaded_model.predict(image)
    print(predictions)
    if predictions[0][0] > 0.5:
        return make_response(jsonify({'NOPE': "Nope, you couldnt make him a cat :/"}), 200)
    else:
        return make_response(jsonify({'flag': 'PoC{WpH3I5aRe4LC4TN0w}'}), 200)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
