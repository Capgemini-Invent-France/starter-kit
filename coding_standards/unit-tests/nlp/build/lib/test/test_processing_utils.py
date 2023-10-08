import pytest
import pandas as pd
import locale

import nlp.processing_utils as processing_utils
import nlp.main.main_processing as main_processing

import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")

from pandas.testing import assert_frame_equal


@pytest.mark.parametrize(
    "input_review,expected_review",
    [
        ("I l'ove chocolate ?!!!", "I love chocolate "),
        ("I love; chocolate !!!", "I love chocolate "),
        ("I lov;e choco,late@ !!!", "I love chocolate "),
        ("I lov;/e choco,la#te@ !!!", "I love chocolate "),
    ],
)
def test_remove_punctuation_from_review(
    input_review: str, expected_review: str
):
    processed_review = processing_utils.remove_punctuation_from_review(
        input_review
    )
    assert processed_review == expected_review


def test_process_review(input_df, processed_df):

    french_stopwords = list(stopwords.words("french")) + ["a", "là", "engie"]
    processed_data = main_processing.process_review(
        input_df,
        note_col="note",
        fournisseur_col="fournisseur",
        verbatim_col="verbatim",
        date_col="date",
        stopwords=french_stopwords,
    )
    assert_frame_equal(processed_data, processed_df)
