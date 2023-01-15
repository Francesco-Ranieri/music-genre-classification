import dotenv
import mlflow
import numpy as np
from pandas import DataFrame
import statistics

from src.features.extract_feature import FeatureExtractor

# will be a rest api
# @predict
from src.models.model_utils import ModelAllowed
from src.visualization.visualization_utils import get_human_readable_label


def predict_genre_music(audio_array):
    """
    :param audio_array:
    :return:
    """
    dotenv.load_dotenv(override=True)

    feature_extractor = FeatureExtractor()
    gtzan_features = feature_extractor.extract_feature(audio_array=audio_array)

    prediction = predict_gtzan_feature(input_data=gtzan_features)
    return get_human_readable_label(prediction)


def predict_gtzan_feature(input_data: DataFrame, model_name: ModelAllowed = ModelAllowed.RANDOM_FOREST):
    """
    :param model_name:
    :param input_data:
    :return:
    """

    if input_data.empty:
        raise ValueError("Cannot predict empty input data")

    model_uri = f"models:/{model_name.value}/latest"
    model_loaded = mlflow.sklearn.load_model(model_uri)
    segment_odd = []
    for _, row in input_data.iterrows():
        row = row.values.reshape(1, -1)
        high_odd_class = get_prediction(model_loaded.predict_proba(row))
        segment_odd.append(high_odd_class)
    return statistics.mode(segment_odd)


def get_prediction(odds):
    hig_prob = np.amax(odds)
    return np.where(odds == hig_prob)[1][0]
