import dotenv
import mlflow
import numpy as np
from feat_extractor import FeatureExtractor

from src.pathUtils import PathUtils
from tests.test_utils.utils import load_test_song


def get_prediction(odds):
    hig_prob = np.amax(odds)
    return np.where(odds == hig_prob)[0][0]


class TestBehavioralModel:
    featureExtractor = FeatureExtractor()

    n_segment = 10

    def _predict_gtzan_feature(self, input_data):

        model_uri = "models:/Random Forest/latest"
        model_loaded = mlflow.sklearn.load_model(model_uri)
        segment_odd = np.zeros(self.n_segment)
        for _, row in input_data.iterrows():
            row = row.values.reshape(1, -1)
            odds = model_loaded.predict_proba(row)
            segment_odd = segment_odd + odds[0]
        return segment_odd / self.n_segment

    def _predict_mfcc_feature(self, input_data):

        model_uri = "models:/CNN/latest"
        model_loaded = mlflow.tensorflow.load_model(model_uri)
        segment_odd = np.zeros(self.n_segment)
        for data in input_data:
            data = np.array([data, ])
            odds = model_loaded.predict(data)
            segment_odd = segment_odd + odds[0]
        return segment_odd / self.n_segment

    def _test_behavior(self, song_path):
        dotenv.load_dotenv(override=True)
        signal, _ = load_test_song(song_path)
        features = self.featureExtractor.extract_feature(signal)
        gtzan_predictions = self._predict_gtzan_feature(features[0])
        mfcc_predictions = self._predict_mfcc_feature(features[1])
        mean_prediction = np.mean(
            (gtzan_predictions, mfcc_predictions), axis=0)
        return get_prediction(mean_prediction)

    def test_correct_behavior(self):
        label_prediction = self._test_behavior(PathUtils.TEST_SONG)

    def test_noise_001(self):
        path = PathUtils.TEST_SONG_AUGMENTED_NOISE.joinpath("noise_0.01.wav")
        label_prediction = self._test_behavior(path)

    def test_noise_01(self):
        path = PathUtils.TEST_SONG_AUGMENTED_NOISE.joinpath("noise_0.1.wav")
        label_prediction = self._test_behavior(path)

    def test_noise_02(self):
        path = PathUtils.TEST_SONG_AUGMENTED_NOISE.joinpath("noise_0.2.wav")
        label_prediction = self._test_behavior(path)

    def test_noise_05(self):
        path = PathUtils.TEST_SONG_AUGMENTED_NOISE.joinpath("noise_0.5.wav")
        label_prediction = self._test_behavior(path)

    def test_noise_1(self):
        path = PathUtils.TEST_SONG_AUGMENTED_NOISE.joinpath("noise_1.wav")
        label_prediction = self._test_behavior(path)

    def test_shift_time_2_right(self):
        path = PathUtils.TEST_SONG_AUGMENTED_SHIFT_TIME.joinpath(
            "shift_2_right.wav")
        label_prediction = self._test_behavior(path)

    def test_shift_time_3_both(self):
        path = PathUtils.TEST_SONG_AUGMENTED_SHIFT_TIME.joinpath(
            "shift_3_both.wav")
        label_prediction = self._test_behavior(path)

    def test_shift_time_6_left(self):
        path = PathUtils.TEST_SONG_AUGMENTED_SHIFT_TIME.joinpath(
            "shift_6_left.wav")
        label_prediction = self._test_behavior(path)

    def test_shift_time_10_both(self):
        path = PathUtils.TEST_SONG_AUGMENTED_SHIFT_TIME.joinpath(
            "shift_10_both.wav")
        label_prediction = self._test_behavior(path)

    def test_shift_time_0_1_both(self):
        path = PathUtils.TEST_SONG_AUGMENTED_SHIFT_TIME.joinpath(
            "shift_0.1_both.wav")
        label_prediction = self._test_behavior(path)

    def test_shift_time_0_2_left(self):
        path = PathUtils.TEST_SONG_AUGMENTED_SHIFT_TIME.joinpath(
            "shift_0.2_left.wav")
        label_prediction = self._test_behavior(path)
