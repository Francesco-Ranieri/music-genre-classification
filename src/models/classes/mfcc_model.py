import json

import dvc.api
import mlflow
from src.pathUtils import PathUtils

from src.data.data_utils import get_processed_data, Dataset
from src.models.classes.base_model import BaseModel
from src.models.model_utils import get_model_from_name


class MfccModel(BaseModel):
    """
    Model for MFCC Dataset
    """

    def __init__(self):
        data = get_processed_data(Dataset.MFCC)

        self.x_train = data["x_train_split"]
        self.y_train = data["y_train_split"]

        self.x_validation = data["x_validation"]
        self.y_validation = data["y_validation"]

        self.x_test = data["x_test"]
        self.y_test = data["y_test"]

        params = dvc.api.params_show()
        self.model_name = params['train']['MFCC']['model-name']

    def train(self):
        """
        :return:
        """

        model = get_model_from_name(self.model_name, Dataset.MFCC)

        with mlflow.start_run(run_name=self.model_name):
            mlflow.autolog()

            history = model.fit(self.x_train,
                      self.y_train,
                      validation_data=(self.x_validation, self.y_validation),
                      batch_size=32,
                      epochs=50)

            mlflow.tensorflow.log_model(model=model,
                                        artifact_path="sklearn-model",
                                        registered_model_name=self.model_name)

            with open(PathUtils.MFCC_REPORTS_PATH, "w+") as report_file:
                report_file.write(json.dumps(history.history, indent=4))

    def test(self):
        pass
