from sklearn.naive_bayes import GaussianNB
from src.data.data_utils import get_dataset
from src.models.evaluation import evaluate_classifier
import mlflow
import dotenv


class ModelTrainer:
    X_train = {}
    y_train = {}
    X_test = {}
    y_test = {}

    def __init__(self):
        data = get_dataset()
        self.X_train = data["X_train"]
        self.y_train = data["y_train"]

        self.X_train_split = data["X_train_split"]
        self.y_train_split = data["y_train_split"]

        self.X_test = data["X_test"]
        self.y_test = data["y_test"]

        self.X_validation = data["X_validation"]
        self.y_validation = data["y_validation"]

    def train_model(self, model, model_name: str = "model"):
        """
        :param model:
        :param model_name:
        :return:
        """

        mlflow.autolog()
        metrics, trained_model = evaluate_classifier(model,
                                                     0,
                                                     self.X_train,
                                                     self.y_train,
                                                     self.X_test,
                                                     self.y_test,
                                                     fit=True)

        mlflow.sklearn.log_model(sk_model=trained_model,
                                 artifact_path="sklearn-model",
                                 registered_model_name=model_name
                                 )


dotenv.load_dotenv(override=True)
experiment_name = "GAUSSIAN_NAIVE_BAYES"
with mlflow.start_run(run_name=experiment_name) as run:
    classifier = GaussianNB()
    model_trainer = ModelTrainer()
    model_trainer.train_model(classifier, experiment_name)
