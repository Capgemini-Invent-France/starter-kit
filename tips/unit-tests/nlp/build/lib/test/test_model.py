import nlp.config as config
import pandas as pd
import numpy as np

from nlp.model_utils import load_model_joblib, save_model_joblib, predict


def test_load_model_joblib(path_prod_model: str, prod_model):
    expected = load_model_joblib(path_prod_model)
    assert prod_model.named_steps.keys() == expected.named_steps.keys()


def test_predict(processed_df: pd.DataFrame, path_prod_model: str):
    predictions = predict(processed_df, path_prod_model)
    expected = np.array(["5", "3", "4"], dtype="<U1")
    assert len(predictions) == 3
    assert expected == predictions
