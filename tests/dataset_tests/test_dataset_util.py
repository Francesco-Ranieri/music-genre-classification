from src.data.data_utils import get_processed_data
from tests.test_utils.test_utils import is_dataset_loaded


class TestDataset:
    """
    Test class for data
    """

    def test_get_processed_data(self):

        data_loaded = {}
        try:
            data_loaded = get_processed_data()
        except FileNotFoundError:
            pass
        finally:
            if not is_dataset_loaded():
                assert data_loaded == {}
            else:
                assert len(data_loaded) > 0
