import pandas as pd
import numpy as np
import librosa

from sklearn import datasets
from sklearn.model_selection import train_test_split

from src.pathUtils import PathUtils, is_dir_empty


def is_dataset_loaded():
    is_loaded = True
    try:
        if is_dir_empty(PathUtils.DATA_PATH):
            is_loaded = False
    except:
        is_loaded = False

    return is_loaded


def load_test_dataset():
    iris = datasets.load_iris()
    X = iris.data[:, 2:]
    y = iris.target

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1, stratify=y)

    return x_train, x_test, y_train, y_test


def load_real_dataset():
    is_loaded = is_dataset_loaded()
    dataset, dataset_x, dataset_y = [], [], []
    if is_loaded:
        dataset = pd.read_csv(PathUtils.GTZAN_DATASET_RAW_PATH, sep=',')
        dataset_x = dataset.drop(['label', 'filename', 'length'], axis=1)
        dataset_y = np.array(dataset.label.astype(int))
        is_loaded = True
    else:
        print("Dowload dataset if you want to run this test !")

    return dataset, dataset_x, dataset_y, is_loaded


def load_test_song():
    path_file = PathUtils.TEST_SONG
    sample_rate = 22050
    return librosa.load(path_file, sr=sample_rate)
