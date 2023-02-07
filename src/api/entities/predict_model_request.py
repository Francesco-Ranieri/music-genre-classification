from typing import List

from pydantic import BaseModel
from src.api.entities.model_allowed_enum import ModelAllowedGTZAN, ModelAllowedMFCC


class PredictModelRequest(BaseModel):
    """
        API REQUEST: \n
        - **audios**: numpy.ndarray = music array \n
        - **gtzan_model**: ModelAllowedGTZAN = model used for predict gtzan feature \n
        - **mfcc_model**: ModelAllowedMFCC = model used for predict mfcc feature
    """

    audios: List = []
    gtzan_model: ModelAllowedGTZAN = ModelAllowedGTZAN.RANDOM_FOREST
    mfcc_model: ModelAllowedMFCC = ModelAllowedMFCC.CNN
