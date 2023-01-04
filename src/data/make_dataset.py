import pickle

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

data_path = Path("../../data/")
dataset_url = data_path.joinpath(Path("raw/features_3_sec.csv"))
processed_path = data_path.joinpath(Path("processed/"))

dataset = pd.read_csv(dataset_url, sep=',')
dataset_X = dataset.drop(['label', 'filename'], axis=1)
dataset_Y = np.array(dataset.label.astype(int))

X_train, X_test, y_train, y_test = train_test_split(dataset_X, dataset_Y, test_size=0.33, random_state=0)
X_train_split, X_validation, y_train_split, y_validation = train_test_split(X_train, y_train, test_size=0.33,
                                                                            random_state=0)
data_to_save = {
    "X_train": X_train,
    "X_test": X_test,
    "y_train": y_train,
    "y_test": y_test,
    "X_train_split": X_train_split,
    "X_validation": X_validation,
    "y_train_split": y_train_split,
    "y_validation": y_validation
}

for k, v in data_to_save.items():
    path_to_save = processed_path.joinpath(f"{k}.pkl")
    print(f"-- Saving {k} in {path_to_save}")
    pickle.dump(v, open(path_to_save, "wb"))
