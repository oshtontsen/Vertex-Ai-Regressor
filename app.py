import pickle
from utils.postprocess import postprocess
from utils.predict import get_prediction
from flask import Flask, jsonify, request

app = Flask(__name__)

MODEL_PATH = 'model.pickle'
model = pickle.load(open(MODEL_PATH, 'rb'))


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    req = request.json.get('instances')

    input_data = req

    # NOTE: No need to preprocess when using the sample_input_clean.json
    # preprocessing
    # text = preprocess(input_data)
    # vector = pre_process.preprocess_tokenizing(text)
    vector = input_data

    # predict
    # TODO: The internal server error arises here
    prediction = get_prediction(model, vector)

    # Postprocess model predictions
    value = postprocess(prediction)

    output = {'predictions': [
        {
            'label': value
        }
    ]
    }
    return jsonify(output)


@app.route('/healthz')
def healthz():
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0')