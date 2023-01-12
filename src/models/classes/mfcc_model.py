import dvc.api
import mlflow

from src.data.data_utils import get_processed_data, Dataset
from src.models.classes.base_model import BaseModel
from src.models.model_utils import get_model_from_name


class MfccModel(BaseModel):
    """
    Model for MFCC Dataset
    """

    def __init__(self):
        data = get_processed_data(Dataset.MFCC)
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
        model_name = params['train']['MFCC']['model-name']
        model = get_model_from_name(model_name, Dataset.MFCC)

        with mlflow.start_run(run_name=model_name):
            mlflow.autolog()

            model.fit(self.x_train_split,
                      self.y_train_split,
                      validation_data=(self.x_validation, self.y_validation),
                      batch_size=32,
                      epochs=50)

            mlflow.tensorflow.log_model(model=model,
                                        artifact_path="sklearn-model",
                                        registered_model_name=model_name)

        def test():
            pass
