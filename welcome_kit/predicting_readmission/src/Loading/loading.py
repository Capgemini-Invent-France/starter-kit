# -*- coding: utf-8 -*-
import pandas as pd
import json
import logging

logger = logging.getLogger("main_logger")

# Description of this script:
# This script implement several loading tools


def read_csv_from_name(conf):
    """
    Calls the read_csv_from_path function giving it a path read in the conf file
    Args:
        conf: conf file

    Returns: dataframe read from csv

    """
    path = conf["Inputs_path"] + conf["path_file"]

    return read_csv_from_path(path)


def read_csv_from_path(path):
    """
    Reads a csv from a path
    Args:
        path: path of the file to read

    Returns: dataframe

    """

    df = pd.read_csv(path, sep=";")
    if df.shape[1] == 1:
        df = pd.read_csv(path, sep=",")
    if "index" in df.columns:
        df = df.drop("index", axis=1)
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)
    logger.debug("file read : " + path)

    return df


def write_preprocessed_csv_from_name(df, conf, name):
    """
    Writes the preprocessed dataframe
    Args:
        df: preprocessed dataframe
        conf: conf file
        name: name you give to the output file

    Returns: "OK"
    """
    selected_dataset = conf["selected_dataset"]
    path = conf["Outputs_path"] + conf["folder_preprocessed"] + name
    df.to_csv(path, sep=";", index=False)
    logger.debug("file wrote : " + path)

    return "OK"


def load_preprocessed_csv_from_name(conf, name):
    """
    Loads the preprocessed dataframe
    Args:
        conf:  conf file
        name: name of the wanted dataset

    Returns: dataframe read

    """
    path = conf["Outputs_path"] + conf["folder_preprocessed"] + name
    df = read_csv_from_path(path)
    logger.debug("file read : " + path)

    return df


def write_dict_json_from_name(dict, conf, name):
    """
    Writes the dictionnary to save
    Args:
        dict: dictionnary to save
        conf: conf file
        name: name you give to the output file

    Returns: "OK"
    """
    path = conf["Outputs_path"] + conf["folder_preprocessed"] + name
    with open(path, "w") as f:
        json.dump(dict, f)
    logger.debug("file wrote : " + path)

    return "OK"


def load_dict_json_from_name(conf, name):
    """
    Loads the dictionnary
    Args:
        conf:  conf file
        name: name of the wanted dictionary

    Returns: dictionary read

    """
    path = conf["Outputs_path"] + conf["folder_preprocessed"] + name
    with open(path, "r") as fp:
        dict = json.load(fp)
    logger.debug("file read : " + path)

    return dict
