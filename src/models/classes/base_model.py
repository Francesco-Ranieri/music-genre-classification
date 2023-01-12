import abc


class BaseModel(object):
    """
    Base Model Class, every model class should implement this methods
    """
    __metaclass__ = abc.ABCMeta

    x_train = {}
    y_train = {}
    x_test = {}
    y_test = {}
    x_train_split = {}
    y_train_split = {}
    x_validation = {}
    y_validation = {}

    def train(self):
        """
        Method for model training
        :return:
        """
        return

    def test(self):
        """
        Method for model testing
        :return:
        """
        return
