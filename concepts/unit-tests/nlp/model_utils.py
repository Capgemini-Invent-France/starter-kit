import datetime
import os
from joblib import dump, load
import pandas as pd

from nlp.utils import is_file_path_exist

from sklearn.pipeline import Pipeline


def load_model_joblib(path: str):
    if is_file_path_exist(path):
        return load(path)
    else:
        raise ValueError("your path doesn't exist, pls provide a valid path")


def save_model_joblib(estimator: Pipeline):

    date_now = datetime.datetime.strftime(
        datetime.datetime.now(), format="%Y_%m_%d"
    )
    filename = f"""models/estimator_{date_now}.joblib"""
    if is_file_path_exist(filename):
        dump(estimator, filename)
    else:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        dump(estimator, filename)


def predict(data: pd.DataFrame, path_model_prod: str):
    model = load_model_joblib(path_model_prod)
    predictions = model.predict(data)

    return predictions
