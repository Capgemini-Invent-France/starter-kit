# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger("main_logger")

import utils as u
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split

# Description of this script:
# main function calling the sub preprocessing function for the dataset selected
# subfunctions applying preprocessing (ex: one hot encoding, dropping etc..)


def main_preprocessing_from_name(df, conf):
    """
    Main Preprocessing function: it launches the correct function in order to preprocess the selected dataset
    Args:
        df: Dataframe
        conf: Conf file

    Returns: Preprocessed Dataframe

    """

    dict_function_preprocess = {
        "bank": "preprocessing_for_bank",
        "orfee": "preprocessing_for_orfee",
        "diabetic": "preprocessing_for_diabetic",
    }

    selected_dataset = conf["selected_dataset"]
    function_preprocess = globals()[dict_function_preprocess[selected_dataset]]
    logger.info(
        "Beginning of preprocessing function: "
        + dict_function_preprocess[selected_dataset]
    )
    df_preprocessed = function_preprocess(df, conf)
    logger.info(
        "End of preprocessing function: " + dict_function_preprocess[selected_dataset]
    )

    return df_preprocessed


def preprocessing_for_diabetic(df, conf):
    """
    Preprocessing for the DIABETIC dataset
    Args:
        df: Diabetic dataset
        conf:  conf file

    Returns: Preprocessed Diabetic Dataset

    """
    # Steps:
    # Clean the output (as 0 or 1)
    # one hot elevel, car, zipcode
    # drop id

    logger.debug("Cleaning Output")
    # Cleaning Output:
    df["readmitted"] = df["readmitted"].map({">30": 1, "<30": 1, "NO": 0})

    logger.debug("mapping Values")
    # Cleaning Other fields:
    for col in ["race", "gender", "weight", "payer_code", "medical_specialty"]:
        df[col] = df[col].str.replace("?", "unknown")

    df["age"] = df["age"].map(
        {
            "unknown": 0,
            "[0-10)": 5,
            "[10-20)": 15,
            "[20-30)": 25,
            "[30-40)": 35,
            "[40-50)": 45,
            "[50-60)": 55,
            "[60-70)": 65,
            "[70-80)": 75,
            "[80-90)": 85,
            "[90-100)": 95,
        }
    )

    df["weight"] = df["weight"].map(
        {
            "unknown": 0,
            "[0-25)": 15,
            "[25-50)": 40,
            "[50-75)": 65,
            "[75-100)": 90,
            "[100-125)": 115,
            "[125-150)": 140,
            "[150-175)": 165,
            "[175-200)": 190,
            ">200": 215,
        }
    )

    logger.debug("One hot Encoding")
    # one hot encoding
    cols = [
        "gender",
        "race",
        "payer_code",
        "medical_specialty",
        "max_glu_serum",
        "A1Cresult",
        "metformin",
        "repaglinide",
        "nateglinide",
        "chlorpropamide",
        "glimepiride",
        "acetohexamide",
        "glipizide",
        "glyburide",
        "tolbutamide",
        "pioglitazone",
        "rosiglitazone",
        "acarbose",
        "miglitol",
        "troglitazone",
        "tolazamide",
        "examide",
        "citoglipton",
        "insulin",
        "glyburide-metformin",
        "glipizide-metformin",
        "glimepiride-pioglitazone",
        "metformin-rosiglitazone",
        "metformin-pioglitazone",
        "change",
        "diabetesMed",
    ]
    categorical_encoder = OrdinalEncoder()
    df[cols] = categorical_encoder.fit_transform(df[cols])
    # Understand each transformation of categorical values
    encoding = categorical_encoder.categories_
    encoding_feature = lambda x: dict(zip(x, range(len(x))))
    encoding_dict = [encoding_feature(feature_elem) for feature_elem in encoding]
    dict_final = dict(zip(cols, encoding_dict))

    logger.debug("Dropping unique columns")
    # Drop id:
    df_preprocessed = df.drop(["encounter_id", "patient_nbr"], axis=1)

    logger.debug("Selection of X and Y")
    # returning columns for train test split
    y_column = u.get_y_column_from_conf(conf)
    X_columns = [x for x in df_preprocessed.columns if x != y_column]

    logger.debug("Verification of float and na values")

    # verification:
    for col in df_preprocessed.columns:
        try:
            df_preprocessed[col] = (
                df_preprocessed[col].astype(str).str.replace(",", ".").astype(float)
            )
        except:
            logger.error(col + " cannot be typed as float")
        if df_preprocessed[col].isna().sum() > 0:
            logger.warning("NA present in " + col)
    logger.info("preprocessing Diabetic ok")

    return df_preprocessed, X_columns, y_column, dict_final


def impute_num(df, cols, cond):
    """
    Replace the NAN in a column by mean by group
    Args:
        df: dataset with NAN
        cols: the columns with the NANs
        cond: variable to group on

    Returns: dataframe with the nan replaced

    """
    for col in cols:
        df = df.set_index([cond])
        means = df.groupby([cond])[col].mean()
        df[col] = df[col].fillna(means)
        df = df.reset_index()
    return df


def encode_dates(data, var):

    # Transform date to dtype format
    df = data.copy()
    df.loc[:, var] = pd.to_datetime(df[var])

    # Encode the date information from the date columns
    df.loc[:, "month"] = df[var].dt.month
    df.loc[:, "year"] = df[var].dt.year
    df.loc[:, "n_days"] = df[var].apply(lambda date: (date - df[var].min()).days)

    return df.drop(var, axis=1)


def basic_split(df, size_of_test, X_columns, y_column):
    """
    Split the dataframe in train, test sets
    Args:
        df: Dataframe to Split
        size_of_test: proportion of test dataset
        X_columns: Columns for the variables
        y_column: Column for the output

    Returns: Train and test datasets for variables and output

    """
    X_train, X_test, y_train, y_test = train_test_split(
        df[X_columns], df[y_column], test_size=size_of_test
    )
    return X_train, X_test, y_train, y_test
