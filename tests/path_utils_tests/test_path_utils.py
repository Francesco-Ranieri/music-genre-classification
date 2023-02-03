import os
from pathlib import Path

from src.pathUtils import PathUtils, is_dir_empty


class TestPathUtils:

    """
    Test class for pathUtils
    """

    def test_path_utils(self):
        assert PathUtils.ROOT_PATH == Path(".").resolve()

        os.mkdir("temp")
        assert is_dir_empty(Path("temp"))
        os.removedirs("temp")
