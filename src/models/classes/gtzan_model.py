import dotenv
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

    model_name = ''

    def __init__(self):
        dotenv.load_dotenv(override=True)
        data = get_processed_data()

        self.x_train = data["x_train_split"]
        self.y_train = data["y_train_split"]

        self.x_validation = data["x_validation"]
        self.y_validation = data["y_validation"]

        params = dvc.api.params_show()
        self.model_name = params['train']['GTZAN']['model-name']

    def train(self):

        """
        :return:
        """

        model = get_model_from_name(self.model_name, Dataset.GTZAN)

        with mlflow.start_run(run_name=self.model_name):
            mlflow.autolog()
            _, trained_model = evaluate_classifier(model,
                                                   0,
                                                   self.x_train.values,
                                                   self.y_train,
                                                   self.x_validation.values,
                                                   self.y_validation,
                                                   fit=True)

            mlflow.sklearn.log_model(sk_model=trained_model,
                                     artifact_path="sklearn-model",
                                     registered_model_name=self.model_name)

    def test(self):
        pass
