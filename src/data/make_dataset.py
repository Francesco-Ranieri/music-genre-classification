import json
import math
import os
import pickle
from io import BytesIO
from pathlib import PosixPath
from zipfile import ZipFile

import librosa
import numpy as np
import pandas as pd
import requests
from sklearn.model_selection import train_test_split

from src.pathUtils import PathUtils, is_dir_empty

SAMPLE_RATE = 22050
TRACK_DURATION = 30
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
NOT_ALLOWED = "jazz.00054.wav"


def _extract_zip(zip_file, destination_path: PosixPath):
    with ZipFile(zip_file) as zip:
        zip.extractall(destination_path)


def download_dataset_if_necessary():
    if is_dir_empty(PathUtils.DATA_RAW_PATH):
        response = requests.get(PathUtils.DATASET_URL)
        _extract_zip(BytesIO(response.content), PathUtils.DATA_RAW_PATH)
        _extract_zip(PathUtils.DATA_RAW_DATASET_GENRES_ZIP, PathUtils.DATA_RAW_DATASET)
        os.remove(PathUtils.DATA_RAW_DATASET_GENRES_ZIP)


def save_gtzan_data(path_to_save: PosixPath = PathUtils.DATA_PROCESSED_PATH):
    dataset = pd.read_csv(PathUtils.GTZAN_DATASET_RAW_PATH, sep=',')
    dataset_x = dataset.drop(['label', 'filename'], axis=1)
    dataset_y = np.array(dataset.label.astype(int))

    x_train, x_test, y_train, y_test = train_test_split(dataset_x, dataset_y, test_size=0.33, random_state=0)
    x_train_split, x_validation, y_train_split, y_validation = train_test_split(x_train, y_train, test_size=0.33,
                                                                                random_state=0)
    data_to_save = {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test,
        "x_train_split": x_train_split,
        "x_validation": x_validation,
        "y_train_split": y_train_split,
        "y_validation": y_validation
    }

    for k, v in data_to_save.items():
        path = path_to_save.joinpath(f"{k}.pkl")
        print(f"-- Saving {k} in {path}")
        pickle.dump(v, open(path, "wb"))


def save_mfcc_data(dataset_path: str,
                   json_path: str,
                   num_mfcc: int = 13,
                   n_fft: int = 2048,
                   hop_length: int = 512,
                   num_segments: int = 5):
    """Extracts MFCCs from music dataset and saves them
        into a json file along witgh genre labels.
        :param dataset_path: Path to dataset
        :param json_path: Path to json file used to save MFCCs
        :param num_mfcc: Number of coefficients to extract
        :param n_fft: Interval we consider to apply FFT. Measured in # of samples
        :param hop_length: Sliding window for FFT. Measured in # of samples
        :param num_segments: Number of segments we want to divide sample tracks into
        :return:
    """

    # dictionary to store mapping, labels, and MFCCs
    data = {
        "mapping": [],
        "labels": [],
        "mfcc": []
    }

    samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    # loop through all genre sub-folder
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # ensure we're processing a genre sub-folder level
        if dirpath is not dataset_path:

            # save genre label (i.e., sub-folder name) in the mapping
            semantic_label = dirpath.split("/")[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing: {}".format(semantic_label))

            # process all audio files in genre sub-dir
            for filename in filenames:

                # load audio file
                file_path = os.path.join(dirpath, filename)
                if filename != NOT_ALLOWED:
                    signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)

                    # process all segments of audio file
                    for num_segment in range(num_segments):

                        # calculate start and finish sample for current segment
                        start = samples_per_segment * num_segment
                        finish = start + samples_per_segment

                        # extract mfcc
                        mfcc = librosa.feature.mfcc(signal[start:finish],
                                                    sample_rate,
                                                    n_mfcc=num_mfcc,
                                                    n_fft=n_fft,
                                                    hop_length=hop_length)
                        mfcc = mfcc.T

                        # store only mfcc feature with expected number of vectors
                        if len(mfcc) == num_mfcc_vectors_per_segment:
                            data["mfcc"].append(mfcc.tolist())
                            data["labels"].append(i - 1)
                            print("{}, segment:{}".format(file_path, num_segment + 1))

    # save MFCCs to json file
    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)


download_dataset_if_necessary()
save_gtzan_data()
save_mfcc_data(PathUtils.MFCC_DATASET_RAW_PATH, PathUtils.MFCC_DATASET_PROCESSED_PATH, num_segments=10)
