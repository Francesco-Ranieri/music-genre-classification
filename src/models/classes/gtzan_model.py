import json

import dvc.api
import mlflow
from src.pathUtils import PathUtils

from src.data.data_utils import get_processed_data, Dataset
from src.models.classes.base_model import BaseModel
from src.models.evaluation import evaluate_classifier
from src.models.model_utils import get_model_from_name


class GtzanModel(BaseModel):

    """
    Model for GTZAN Dataset
    """

    def __init__(self):
        data = get_processed_data()

        self.x_train = data["x_train_split"]
        self.y_train = data["y_train_split"]

        self.x_validation = data["x_validation"]
        self.y_validation = data["y_validation"]

        self.x_test = data["x_test"]
        self.y_test = data["y_test"]

        params = dvc.api.params_show()
        self.model_name = params['train']['GTZAN']['model-name']

    def train(self):
        """
        :return:
        """

        model = get_model_from_name(self.model_name, Dataset.GTZAN)

        with mlflow.start_run(run_name=self.model_name):
            mlflow.autolog()
            metrics, trained_model = evaluate_classifier(model,
                                                         0,
                                                         self.x_train.values,
                                                         self.y_train,
                                                         self.x_validation.values,
                                                         self.y_validation,
                                                         fit=True)

            mlflow.sklearn.log_model(sk_model=trained_model,
                                     artifact_path="sklearn-model",
                                     registered_model_name=self.model_name)

            with open(PathUtils.GTZAN_REPORTS_PATH, "w+") as report_file:
                report_file.write(json.dumps(metrics, indent=4))

    def test(self):
        pass
