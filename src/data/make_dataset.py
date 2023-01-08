import pickle

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path, PosixPath
import json
import os
import math
import librosa

DATA_PATH = Path("../../data/")
PROCESSED_PATH = DATA_PATH.joinpath(Path("processed/"))

GTZA_DATASET_PATH = DATA_PATH.joinpath(Path("raw/features_3_sec.csv"))
MFCC_DATASET_PATH = DATA_PATH.joinpath(Path("raw/genres_original/"))

SAMPLE_RATE = 22050
TRACK_DURATION = 30  # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
not_allowed = "jazz.00054.wav"


def save_gtzan_data(path_to_save: PosixPath = PROCESSED_PATH):
    dataset = pd.read_csv(GTZA_DATASET_PATH, sep=',')
    dataset_X = dataset.drop(['label', 'filename'], axis=1)
    dataset_Y = np.array(dataset.label.astype(int))

    X_train, X_test, y_train, y_test = train_test_split(dataset_X, dataset_Y, test_size=0.33, random_state=0)
    X_train_split, X_validation, y_train_split, y_validation = train_test_split(X_train, y_train, test_size=0.33,
                                                                                random_state=0)
    data_to_save = {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "X_train_split": X_train_split,
        "X_validation": X_validation,
        "y_train_split": y_train_split,
        "y_validation": y_validation
    }

    for k, v in data_to_save.items():
        path = path_to_save.joinpath(f"{k}.pkl")
        print(f"-- Saving {k} in {path}")
        pickle.dump(v, open(path, "wb"))


def save_mfcc_data(dataset_path: str, json_path: str, num_mfcc: int = 13, n_fft: int = 2048, hop_length: int = 512,
                   num_segments: int = 5):
    """Extracts MFCCs from music dataset and saves them into a json file along witgh genre labels.
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
            for f in filenames:

                # load audio file
                file_path = os.path.join(dirpath, f)
                if f != not_allowed:
                    signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)

                    # process all segments of audio file
                    for d in range(num_segments):

                        # calculate start and finish sample for current segment
                        start = samples_per_segment * d
                        finish = start + samples_per_segment

                        # extract mfcc
                        mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                                    hop_length=hop_length)
                        mfcc = mfcc.T

                        # store only mfcc feature with expected number of vectors
                        if len(mfcc) == num_mfcc_vectors_per_segment:
                            data["mfcc"].append(mfcc.tolist())
                            data["labels"].append(i - 1)
                            print("{}, segment:{}".format(file_path, d + 1))

    # save MFCCs to json file
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


print("here")
# save_gtzan_data()
# save_mfcc_data(MFCC_DATASET_PATH, PROCESSED_PATH.joinpath("mfcc_dataset.json"), num_segments=10)
