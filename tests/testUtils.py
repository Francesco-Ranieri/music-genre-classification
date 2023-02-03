from sklearn import datasets
from sklearn.model_selection import train_test_split
from src.pathUtils import PathUtils, is_dir_empty


def load_test_dataset():
    iris = datasets.load_iris()
    X = iris.data[:, 2:]
    y = iris.target

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1, stratify=y)

    return x_train, x_test, y_train, y_test


def is_dataset_loaded():
    is_loaded = True
    try:
        if is_dir_empty(PathUtils.DATA_PROCESSED_GTZAN_PATH):
            is_loaded = False
    except:
        is_loaded = False

    return is_loaded
