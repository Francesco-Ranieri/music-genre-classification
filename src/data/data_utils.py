import os
import pickle
from enum import Enum

from src.pathUtils import PathUtils


class Dataset(Enum):
    GTZAN = "gtzan"
    MFCC = "mfcc"


def get_processed_data(dataset: Enum = Dataset.GTZAN):
    """
    :param dataset: Enum Gtazan or MFCC
    :return:
    """

    path = PathUtils.DATA_PROCESSED_GTZAN_PATH
    if dataset == Dataset.MFCC:
        path = PathUtils.DATA_PROCESSED_MFCC_PATH
    data_to_load = [file_name for file_name in os.listdir(
        path) if ".pkl" in file_name]

    data_loaded = {}

    for file_name in data_to_load:
        path_to_load = path.joinpath(f"{file_name}")
        print(f"-- Loading {file_name}")
        key = file_name.replace(".pkl", "")
        data_loaded[key] = pickle.load(open(path_to_load, 'rb'))

    return data_loaded
