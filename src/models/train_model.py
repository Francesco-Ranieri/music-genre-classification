import pandas as pd
import pickle
from pathlib import Path
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import os
import dagshub


# Path of the prepared data folder
input_folder_path = Path("C:/Users/ranie/Desktop/ml-boilerplate/data/raw")

# Read training dataset
X_train = pd.read_csv(input_folder_path / "test.csv")
y_train = pd.read_csv(input_folder_path / "test.csv")

# ============== #
# MODEL TRAINING #
# ============== #

# Specify the model
algorithm = RandomForestRegressor

# For the sake of reproducibility, I set the `random_state`
model = algorithm(random_state=0)

with dagshub.dagshub_logger() as logger:

    # Then I fit the model to the training data
    model.fit(X_train, y_train)
    logger.log_hyperparams({'model': model.get_params()})

    # Eventually I save the model as a pickle file
    Path("models").mkdir(exist_ok=True)
    output_folder_path =  Path("C:/Users/ranie/Desktop/ml-boilerplate/models")

    with open(output_folder_path / "model.pkl", "wb") as pickle_file:
        pickle.dump(model, pickle_file)
        print("SAVED!!")