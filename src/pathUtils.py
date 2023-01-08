from pathlib import Path


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
    DATA_PATH = ROOT_PATH.joinpath("data")
    DATA_EXTERNAL_PATH = DATA_PATH.joinpath("external")
    DATA_INTERIM_PATH = DATA_PATH.joinpath("interim")
    DATA_PROCESSED_PATH = DATA_PATH.joinpath("processed")
    DATA_RAW_PATH = DATA_PATH.joinpath("raw")
    SRC_PATH = ROOT_PATH.joinpath("src")
