import pandas as pd
import nlp.processing_utils as processing_utils


def process_review(
    df: pd.DataFrame,
    note_col: str,
    fournisseur_col: str,
    verbatim_col: str,
    date_col: str,
    stopwords: list,
) -> pd.DataFrame:

    df = processing_utils.check_duplicates(df)
    df[note_col] = df[note_col].apply(processing_utils.extract_mark)
    df[date_col] = df[date_col].apply(processing_utils.extract_date)
    df[fournisseur_col] = df[fournisseur_col].apply(
        processing_utils.extract_fournisseur
    )
    df[verbatim_col] = df[verbatim_col].apply(processing_utils.lower_reviews)
    df[verbatim_col] = df[verbatim_col].apply(
        processing_utils.remove_punctuation_from_review
    )
    df[verbatim_col] = df[verbatim_col].apply(
        processing_utils.remove_stop_words, args=(stopwords,)
    )

    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month

    df = df.drop(["titre", date_col], axis=1)

    return df
