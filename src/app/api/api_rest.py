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


def predict_genre_music(audio_array,
                        gtzan_model: ModelAllowed = ModelAllowed.RANDOM_FOREST,
                        mfcc_model: ModelAllowed = ModelAllowed.CNN):
    """
    :param mfcc_model:
    :param gtzan_model:
    :param audio_array:
    :return:
    """
    dotenv.load_dotenv(override=True)

    feature_extractor = FeatureExtractor()
    gtzan_features, mfcc_features = feature_extractor.extract_feature(audio_array=audio_array)

    gtzan_predictions = predict_gtzan_feature(input_data=gtzan_features, model_name=gtzan_model)
    mfcc_predictions = predict_mfcc_feature(input_data=mfcc_features, model_name=mfcc_model)

    mean_prediction = np.mean((gtzan_predictions, mfcc_predictions), axis=0)
    label_prediction = get_prediction(mean_prediction)

    return get_human_readable_label(label_prediction)


def predict_gtzan_feature(input_data: DataFrame, model_name: ModelAllowed):
    """
    :param model_name:
    :param input_data:
    :return:
    """

    if input_data.empty:
        raise ValueError("Cannot predict empty input data")

    model_uri = f"models:/{model_name.value}/latest"
    model_loaded = mlflow.sklearn.load_model(model_uri)
    segment_odd = np.zeros(10)
    for _, row in input_data.iterrows():
        row = row.values.reshape(1, -1)
        odds = model_loaded.predict_proba(row)
        segment_odd = segment_odd + odds[0]
    return segment_odd/10


def predict_mfcc_feature(input_data, model_name: ModelAllowed):

    """
    :param input_data:
    :param model_name:
    :return:
    """

    model_uri = f"models:/{model_name.value}/latest"
    model_loaded = mlflow.tensorflow.load_model(model_uri)
    segment_odd = np.zeros(10)
    for data in input_data:
        data = np.array([data, ])
        odds = model_loaded.predict(data)
        segment_odd = segment_odd + odds[0]
    return segment_odd/10


def get_prediction(odds):

    """
    :param odds:
    :return:
    """

    hig_prob = np.amax(odds)
    return np.where(odds == hig_prob)[0][0]
