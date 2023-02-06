from src.models.evaluation import evaluate_classifier

from src.data.data_utils import Dataset

from src.models.model_utils import get_model_from_name
from sklearn import ensemble

from tests.test_utils.mock_dataset import load_test_dataset


class TestModels:
    """
    Test class for src/Models folder
    """

    def test_model_utils(self):
        model = get_model_from_name("Random Forest", Dataset.GTZAN)
        assert model is not None
        assert isinstance(model, ensemble.RandomForestClassifier)

    def test_model_evaluation_split(self):
        model = ensemble.RandomForestClassifier()
        x_train, x_test, y_train, y_test = load_test_dataset()

        metrics, trained_model = evaluate_classifier(model,
                                                     0,
                                                     x_train,
                                                     y_train,
                                                     x_test,
                                                     y_test,
                                                     fit=True)
        assert metrics is not None
        assert trained_model is not None
        assert metrics["accuracy"] is not None
        assert metrics["precision"] is not None
        assert metrics["recall"] is not None
        assert metrics["f_micro"] is not None
        assert metrics["f_macro"] is not None
