import pickle


def save_model(model):
    """Pickle model"""
    with open('model.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        # NOTE: protocol number offers file compatibility across dif versions of python
        pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)