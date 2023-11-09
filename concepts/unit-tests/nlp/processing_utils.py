import re
import datetime
import string
import pandas as pd


def extract_mark(note: str) -> str:
    string_first_number = re.search(r"\d+", note).group()
    return float(string_first_number)


def extract_date(date: str, key_split_word="expérience: ") -> str:
    dateInStringFormat = date.split(key_split_word, 1)[-1]
    date = datetime.datetime.strptime(dateInStringFormat, "%d %B %Y")
    return date


def lower_reviews(review: str) -> str:
    return review.lower()


def extract_fournisseur(fournisseur: str) -> str:
    name = fournisseur.split("/")[-1].split(".")[0]
    return name


def remove_punctuation_from_review(review):
    exclude = set(string.punctuation)
    review = "".join(ch for ch in review if ch not in exclude)
    return review


def remove_stop_words(review: str, stop_words: list) -> str:
    return " ".join(word for word in review.split() if word not in stop_words)


def check_duplicates(df: pd.DataFrame):
    nb_duplicated = df.duplicated().sum()
    if nb_duplicated > 0:
        print(
            f"""there is {nb_duplicated} duplicates in the database, we will drop them"""
        )
        df = df.drop_duplicates()
        return df
    else:
        return df
