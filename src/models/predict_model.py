import argparse

import dotenv
import dvc.api
import mlflow

from src.data.data_utils import Dataset
from src.data.data_utils import get_processed_data
from src.models.evaluation import evaluate_classifier


def retrieve_model_uri_dvc(_model_type: Dataset):
    """
    :param model_type: model type 'GTZAN' or 'MFCC'
    :return: model_uri for dvc
    """

    params = dvc.api.params_show()
    _model_type = _model_type.value.upper()
    model_name = params['test'][_model_type]['model-name']
    return f"models:/{model_name}/latest"


dotenv.load_dotenv(override=True)
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", "-d",
                    help="Set testing flow based on dataset (MFCC or GTZAN)")
args = parser.parse_args()
model_type = args.dataset

data = get_processed_data(Dataset(model_type))
x_test = data['x_test']
y_test = data['y_test']
model_uri = retrieve_model_uri_dvc(Dataset(model_type))

if args.dataset == Dataset.GTZAN.value:
    model_loaded = mlflow.sklearn.load_model(model_uri)
    evaluate_classifier(model_loaded, 0, [], [], x_test, y_test, fit=False)

elif args.dataset == Dataset.MFCC.value:
    model_loaded = mlflow.tensorflow.load_model(model_uri)
    model_loaded.evaluate(x_test, y_test)
