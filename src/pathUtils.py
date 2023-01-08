from pathlib import Path


class PathUtils:
    ROOT_PATH = Path(".").resolve()
    DATA_PATH = ROOT_PATH.joinpath("data")
    DATA_EXTERNAL_PATH = DATA_PATH.joinpath("external")
    DATA_INTERIM_PATH = DATA_PATH.joinpath("interim")
    DATA_PROCESSED_PATH = DATA_PATH.joinpath("processed")
    DATA_RAW_PATH = DATA_PATH.joinpath("raw")
    SRC_PATH = ROOT_PATH.joinpath("src")

