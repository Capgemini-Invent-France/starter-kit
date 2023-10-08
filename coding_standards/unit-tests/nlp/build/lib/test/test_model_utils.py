import nlp.config as config
import pandas as pd
import numpy as np

from numpy.testing import assert_array_equal

from nlp.model_utils import load_model_joblib, save_model_joblib, predict


def test_load_model_joblib(path_prod_model: str, prod_model):
    expected = load_model_joblib(path_prod_model)
    assert prod_model.named_steps.keys() == expected.named_steps.keys()


def test_predict(processed_df: pd.DataFrame, path_prod_model: str):
    predictions = predict(processed_df["verbatim"], path_prod_model)
    expected = np.array(["1.0", "1.0"], dtype=object)
    assert len(predictions) == 2
    assert_array_equal(expected, predictions)
