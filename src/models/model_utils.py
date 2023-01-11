from enum import Enum

import sklearn


class ModelAllowed(Enum):
    GAUSSIAN_NB = 'Gaussian NB'


def get_model_from_name(model_name):
    """
    :param model_name: name of the model ['Gaussian NB', ]
    :return:
    """

    if model_name == ModelAllowed.GAUSSIAN_NB.value:
        model = sklearn.naive_bayes.GaussianNB()
    else:
        raise ValueError("Model name provided is not allowed")

    return model
