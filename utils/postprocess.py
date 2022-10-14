def postprocess(predictions):
    """Model predictions are returned as np arrays which are not JSON serializable, thus predicitons must be converted
    # to list"""
    return list(predictions)
