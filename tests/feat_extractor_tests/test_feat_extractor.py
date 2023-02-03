import librosa

from src.feat_extractor import FeatureExtractor
from src.pathUtils import PathUtils


class TestFeatureExtractor:
    """
    Test class for feat_extractor
    """

    featureExtractor = FeatureExtractor()
    path_file = PathUtils.TEST_SONG
    sample_rate = 22050

    def test_extract_feature(self):
        signal, _ = librosa.load(self.path_file, sr=self.sample_rate)
        features = self.featureExtractor.extract_feature(signal)

        assert len(features)
        assert len(features) == 2
        assert features[0].shape == (10, 58)
        assert features[1].shape == (10, 130, 13, 1)
