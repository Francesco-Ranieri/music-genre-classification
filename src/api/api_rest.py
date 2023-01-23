import dotenv
import mlflow
import numpy as np
from fastapi import FastAPI
from feat_extractor import FeatureExtractor
from pandas import DataFrame
from src.api.entities.predict_model_request import PredictModelRequest
from src.api.entities.model_allowed_enum import ModelAllowed
import logging as log

app = FastAPI()


@app.get("/")
async def read_main():
    return {"Server is working !"}


@app.post("/predict_music")
async def predict_genre_music(predict_request: PredictModelRequest):
    """
    :param predict_request:
    :return:
    """

    req = predict_request.dict()
    dotenv.load_dotenv(override=True)
    feature_extractor = FeatureExtractor()

    gtzan_features, mfcc_features = feature_extractor.extract_feature(
        audio_array=req["audio_array"])
    gtzan_predictions = predict_gtzan_feature(
        input_data=gtzan_features, model_name=req["gtzan_model"])
    mfcc_predictions = predict_mfcc_feature(
        input_data=mfcc_features, model_name=req["mfcc_model"])

    mean_prediction = np.mean((gtzan_predictions, mfcc_predictions), axis=0)
    label_prediction = get_prediction(mean_prediction)

    print(get_human_readable_label(label_prediction))
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
    return segment_odd / 10


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
    return segment_odd / 10


def get_prediction(odds):
    """
    :param odds:
    :return:
    """

    hig_prob = np.amax(odds)
    return np.where(odds == hig_prob)[0][0]


label = ['blues',
         'classical',
         'country',
         'disco',
         'hip hop',
         'jazz',
         'metal',
         'pop',
         'reggae',
         'rock']


def get_human_readable_label(label_number: int):
    return label[label_number]
