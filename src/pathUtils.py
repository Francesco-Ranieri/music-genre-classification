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
    A path utils class.

    ...

    Attributes
    ----------
    ROOT_PATH : Path
        root path
    DATA_PATH : Path
        data path
    DATA_EXTERNAL_PATH : Path
        data path
    DATA_INTERIM_PATH : Path
        data interim path
    DATA_PROCESSED_PATH : Path
        data processed path
    DATA_RAW_PATH : Path
        data raw path
    SRC_PATH : Path
        data src path

    Methods
    -------
    """

    ROOT_PATH = Path(".").resolve()
    SRC_PATH = ROOT_PATH.joinpath("src")

    DATA_PATH = ROOT_PATH.joinpath("data")
    DATA_PROCESSED_PATH = DATA_PATH.joinpath("processed")
    DATA_PROCESSED_GTZAN_PATH = DATA_PROCESSED_PATH.joinpath("gtzan_data")
    DATA_PROCESSED_MFCC_PATH = DATA_PROCESSED_PATH.joinpath("mfcc_data")
    MFCC_DATASET_PROCESSED_PATH = DATA_PROCESSED_PATH.joinpath(
        Path("mfcc_dataset.json"))

    DATA_RAW_PATH = DATA_PATH.joinpath("raw")
    DATA_RAW_DATASET = DATA_RAW_PATH.joinpath("dataset")
    DATA_RAW_DATASET_GENRES_ZIP = DATA_RAW_DATASET.joinpath("genres.zip")
    GTZAN_DATASET_RAW_PATH = DATA_RAW_DATASET.joinpath(
        Path("features_3_sec.csv"))
    MFCC_DATASET_RAW_PATH = DATA_RAW_DATASET.joinpath(Path("genres_original"))

    DATASET_URL = "https://drive.google.com/uc?id=1hCOpQpQbDEhswsuSchSpVDmW6w-VfJ8X&export=" \
                  "download&confirm=t&uuid=1d2e5d2c-ecbb-4bbd-be85-e17bd545e4af"
