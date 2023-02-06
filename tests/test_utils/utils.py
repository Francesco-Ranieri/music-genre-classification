import librosa
import numpy as np
import pandas as pd
from deepchecks import Dataset

from src.data.data_utils import get_processed_data
from src.pathUtils import PathUtils, is_dir_empty

from src.data.data_utils import Dataset as DatasetType


def is_dataset_loaded():
    is_loaded = True
    try:
        if is_dir_empty(PathUtils.DATA_PATH):
            is_loaded = False
    except:
        is_loaded = False

    return is_loaded


def load_real_gtzan_dataset():
    ds_dataset = []

    if is_dataset_loaded():
        dataset = pd.read_csv(PathUtils.GTZAN_DATASET_RAW_PATH, sep=',')
        dataset = dataset.drop(['filename', 'length'], axis=1)

        ds_dataset = Dataset(dataset, label="label")

    else:
        print("Dowload gtzan dataset if you want to run this test !")

    return ds_dataset


def load_real_mfcc_dataset():
    ds_dataset = []

    if is_dataset_loaded():

        data_loaded = get_processed_data(DatasetType.MFCC)

        """
            In order to test integrity of MFCC dataset,
            the dataset must be converted into a tabular
            format and so into a pandas dataFrame.
        """

        x_train = np.squeeze(data_loaded['x_train'], axis=3)
        y_train = data_loaded['y_train']
        x_test = np.squeeze(data_loaded['x_test'], axis=3)
        y_test = data_loaded['y_test']
        train_dimension = x_train.shape
        test_dimension = x_test.shape

        x_dataset = []
        y_dataset = []

        for i in range(train_dimension[0]):
            for y in range(train_dimension[1]):
                x_current = np.append(x_train[i][y][:], y_train[i])
                x_dataset.append(x_current)

        for i in range(test_dimension[0]):
            for y in range(test_dimension[1]):
                y_current = np.append(x_test[i][y][:], y_test[i])
                y_dataset.append(y_current)

        x_dataset.extend(y_dataset)

        columns = [f"mfcc_{i}" for i in range(13)]
        columns.append("label")
        pd_dataset = pd.DataFrame(x_dataset, columns=columns)

        ds_dataset = Dataset(pd_dataset, label="label")
    else:
        print("Dowload mfcc dataset if you want to run this test !")

    return ds_dataset


def load_test_song(path_file=PathUtils.TEST_SONG):
    sample_rate = 22050
    return librosa.load(path_file, sr=sample_rate)
