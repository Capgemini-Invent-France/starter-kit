import pytest
import pandas as pd
import locale

import nlp.processing_utils as processing_utils
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")


def test_extract_mark():

    # Given
    input_string = "Noté 1 sur 5"
    expected = 1

    # When
    result = processing_utils.extract_mark(input_string)

    # Then
    assert result == expected


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
