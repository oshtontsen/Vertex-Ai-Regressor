from sklearn.tree import DecisionTreeRegressor


def train(melbourne_data):
    """Train model"""
    # Define model. Specify a number for random_state to ensure same results each run
    melbourne_model = DecisionTreeRegressor(random_state=1)
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = melbourne_data[melbourne_features]
    y = melbourne_data.Price

    # Fit model
    melbourne_model.fit(X, y)
    return melbourne_model