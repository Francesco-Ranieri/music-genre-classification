import dvc.api
import mlflow

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
        self.x_train = data["x_train"]
        self.y_train = data["y_train"]

        self.x_train_split = data["x_train_split"]
        self.y_train_split = data["y_train_split"]

        self.x_test = data["x_test"]
        self.y_test = data["y_test"]

        self.x_validation = data["x_validation"]
        self.y_validation = data["y_validation"]

    def train(self):

        """
        :return:
        """

        params = dvc.api.params_show()
        model_name = params['train']['GTZAN']['model-name']
        model = get_model_from_name(model_name, Dataset.GTZAN)

        with mlflow.start_run(run_name=model_name):
            mlflow.autolog()
            _, trained_model = evaluate_classifier(model,
                                                   0,
                                                   self.x_train,
                                                   self.y_train,
                                                   self.x_test,
                                                   self.y_test,
                                                   fit=True)

            mlflow.sklearn.log_model(sk_model=trained_model,
                                     artifact_path="sklearn-model",
                                     registered_model_name=model_name)

        def test():
            pass
