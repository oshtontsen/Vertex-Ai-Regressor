import json
import pickle


def get_prediction(model, input_data):
    """Predict on data from input json"""
    return model.predict(input_data)


if __name__ == '__main__':
    # ---
    # DEBUG
    # Predict on input csv
    # ---
    # import pandas as pd
    # df = pd.read_csv('data/melb_data.csv')
    # melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    # df = df[melbourne_features].head()
    # predictions = predict(df)
    # ---
    MODEL_PATH = '../model.pickle'
    model = pickle.load(open(MODEL_PATH, 'rb'))

    # Read in input json
    f = open('../data/sample_input_clean.json', 'r')
    input_data = json.loads(f.read())
    input_data = input_data['instances']
    predictions = get_prediction(model, input_data)

    # Display predictions
    for prediction in predictions:
        print("[OUTPUT]: The model predicted {}".format(prediction))
