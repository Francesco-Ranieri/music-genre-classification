from sklearn.naive_bayes import GaussianNB
import mlflow
import dotenv

from src.data.data_utils import get_dataset
from src.models.evaluation import evaluate_classifier


class ModelTrainer:
    x_train = {}
    y_train = {}
    x_test = {}
    y_test = {}
    x_train_split = {}
    y_train_split = {}
    x_validation = {}
    y_validation = {}

    def __init__(self):
        data = get_dataset()
        self.x_train = data["x_train"]
        self.y_train = data["y_train"]

        self.x_train_split = data["x_train_split"]
        self.y_train_split = data["y_train_split"]

        self.x_test = data["x_test"]
        self.y_test = data["y_test"]

        self.x_validation = data["x_validation"]
        self.y_validation = data["y_validation"]

    def train_model(self, model, model_name: str = "model"):
        """
        :param model:
        :param model_name:
        :return:
        """

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
                                 registered_model_name=model_name
                                 )


dotenv.load_dotenv(override=True)
EXPERIMENT_NAME = "GAUSSIAN_NAIVE_BAYES"
with mlflow.start_run(run_name=EXPERIMENT_NAME) as run:
    classifier = GaussianNB()
    model_trainer = ModelTrainer()
    model_trainer.train_model(classifier, EXPERIMENT_NAME)
