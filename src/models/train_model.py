import argparse

import dotenv

from src.data.data_utils import Dataset
from src.models.classes.gtzan_model import GtzanModel
from src.models.classes.mfcc_model import MfccModel

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", "-d", help="Set training flow based on dataset")
args = parser.parse_args()

if args.dataset == Dataset.GTZAN.value:
    model = GtzanModel()
elif args.dataset == Dataset.MFCC.value:
    model = MfccModel()
else:
    raise SystemError("Model not found")

dotenv.load_dotenv(override=True)
model.train()
