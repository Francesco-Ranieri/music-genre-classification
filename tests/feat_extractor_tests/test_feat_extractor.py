from src.feat_extractor import FeatureExtractor
from tests.test_utils.test_utils import load_test_song


class TestFeatureExtractor:
    """
    Test class for feat_extractor
    """

    featureExtractor = FeatureExtractor()

    def test_extract_feature(self):
        signal, _ = load_test_song()
        features = self.featureExtractor.extract_feature(signal)

        assert len(features)
        assert len(features) == 2
        assert features[0].shape == (10, 58)
        assert features[1].shape == (10, 130, 13, 1)
