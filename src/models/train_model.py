from pathlib import Path
import pickle
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import dagshub

input_folder_path = Path("C:/Users/ranie/Desktop/ml-boilerplate/data/raw")

X_train = pd.read_csv(input_folder_path / "test.csv")
y_train = pd.read_csv(input_folder_path / "test.csv")

model = RandomForestRegressor(random_state=0)

with dagshub.dagshub_logger() as logger:
    model.fit(X_train, y_train)
    logger.log_hyperparams({'model': model.get_params()})
    Path("models").mkdir(exist_ok=True)
    output_folder_path = Path("C:/Users/ranie/Desktop/ml-boilerplate/models")

    with open(output_folder_path / "model.pkl", "wb") as pickle_file:
        pickle.dump(model, pickle_file)
        print("SAVED!!")
