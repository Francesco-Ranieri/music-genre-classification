from src.api.music_prediction import get_prediction, get_human_readable_label


class TestApi:
    """
    Test class for api
    """

    def test_get_prediction(self):
        index = get_prediction([1, 2, 10, 4, 5])
        assert index == 2

    def test_get_human_readable_label(self):
        label = get_human_readable_label(0)
        assert label == "blues"
