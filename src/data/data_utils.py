import pickle
import os
from enum import Enum

from src.pathUtils import PathUtils

PROCESSED_PATH = PathUtils.DATA_PROCESSED_PATH


class Dataset(Enum):
    GTZAN = "gtzan"
    MFCC = "mfcc"


def get_dataset(dataset: Enum = Dataset.GTZAN):
    data_to_load = [file_name for file_name in os.listdir(PROCESSED_PATH) if ".pkl" in file_name]

    if dataset == Dataset.MFCC:
        data_to_load = [file_name for file_name in os.listdir(PROCESSED_PATH) if ".json" in file_name]

    data_loaded = {}

    for file_name in data_to_load:
        path_to_load = PROCESSED_PATH.joinpath(f"{file_name}")
        print(f"-- Loading {file_name}")
        key = file_name.replace(".pkl", "").replace(".json", "")
        data_loaded[key] = pickle.load(open(path_to_load, 'rb'))

    return data_loaded
