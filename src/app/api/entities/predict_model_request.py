from typing import List

from pydantic import BaseModel
from src.models.model_utils import ModelAllowed


class PredictModelRequest(BaseModel):
    audio_array: List = []
    gtzan_model: ModelAllowed = ModelAllowed.RANDOM_FOREST
    mfcc_model: ModelAllowed = ModelAllowed.CNN
