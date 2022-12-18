import locale

import nlp.main.main_processing as main_processing

import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")

from pandas.testing import assert_frame_equal


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
