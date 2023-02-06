from pathlib import Path
import os


def is_dir_empty(path: Path) -> bool:
    """
    :param path: dir to check
    """

    dir_files = os.listdir(path)
    return len(dir_files) == 0


class PathUtils:

    """
    A path utils class
    """

    # ROOT FOLDER
    ROOT_PATH = Path(".").resolve()
    SRC_PATH = ROOT_PATH.joinpath("src")

    # SRC/REPORTS FOLDER AND FILES
    REPORTS_PATH = ROOT_PATH.joinpath("reports")
    REPORTS_HISTORY_PATH = REPORTS_PATH.joinpath("history")
    GTZAN_REPORTS_PATH = REPORTS_HISTORY_PATH.joinpath("gtzan_history.json")
    MFCC_REPORTS_PATH = REPORTS_HISTORY_PATH.joinpath("mfcc_history.json")

    DATA_PATH = ROOT_PATH.joinpath("data")

    # SRC/DATA/PROCESSED FOLDER AND FILES
    DATA_PROCESSED_PATH = DATA_PATH.joinpath("processed")
    DATA_PROCESSED_GTZAN_PATH = DATA_PROCESSED_PATH.joinpath("gtzan_data")
    DATA_PROCESSED_MFCC_PATH = DATA_PROCESSED_PATH.joinpath("mfcc_data")
    MFCC_DATASET_PROCESSED_PATH = DATA_PROCESSED_PATH.joinpath(
        Path("mfcc_dataset.json"))

    # SRC/DATA/RAW FOLDER AND FILES
    DATA_RAW_PATH = DATA_PATH.joinpath("raw")
    DATA_RAW_DATASET = DATA_RAW_PATH.joinpath("dataset")
    DATA_RAW_DATASET_GENRES_ZIP = DATA_RAW_DATASET.joinpath("genres.zip")
    GTZAN_DATASET_RAW_PATH = DATA_RAW_DATASET.joinpath(
        Path("features_3_sec.csv"))
    MFCC_DATASET_RAW_PATH = DATA_RAW_DATASET.joinpath(Path("genres_original"))

    # DRIVE URL
    DATASET_URL = "https://drive.google.com/uc?id=1hCOpQpQbDEhswsuSchSpVDmW6w-VfJ8X&export=" \
                  "download&confirm=t&uuid=1d2e5d2c-ecbb-4bbd-be85-e17bd545e4af"

    # TEST SONG
    TEST_RESOURCES = ROOT_PATH.joinpath("tests/resources")
    TEST_SONG = TEST_RESOURCES.joinpath("hip_hop_test.wav")
    TEST_SONG_AUGMENTED = TEST_RESOURCES.joinpath("augmented")
    TEST_SONG_AUGMENTED_NOISE = TEST_SONG_AUGMENTED.joinpath("noise")
    TEST_SONG_AUGMENTED_SHIFT_TIME = TEST_SONG_AUGMENTED.joinpath("shift_time")
