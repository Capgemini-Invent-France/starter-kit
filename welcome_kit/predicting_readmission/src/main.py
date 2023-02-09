################## Importing libraries ####################
import os
import sys

from src.Loading import loading
from src.Preprocessing import preprocessing
from src.Modeling import modeling
from src.Evaluation import evaluation
from src.Interpretability import interpretability
from src.Utils import utils as u

import argparse
import json
from time import time

import logging

## The parser allow to get arguments from the command line in order to launch only selected steps
parser = argparse.ArgumentParser(
    description="DS&DE Basics ML Project",
    epilog="This has been developped by Capgemini Invent",
)

parser.add_argument("--step", help="integer that tells which step to run", default=-1)
parser.add_argument(
    "--step_from",
    help="integer that tells from which step to run main. It then run all the steps from step_from",
    default=0,
)
parser.add_argument(
    "--step_list", help="list of integer that tells which steps to run", default=[]
)

parser.add_argument(
    "--pathconf", help="path to conf file", default="params/conf/conf.json"
)

args = parser.parse_args()
step = int(args.step)
step_from = int(args.step_from)
step_list = args.step_list
path_conf = args.pathconf

# path_conf ='../conf/conf.json'
conf = json.load(open(path_conf, "r"))

path_log = conf["path_log"]  # "../log/my_log_file.txt"
log_level = conf["log_level"]  # "DEBUG"

# instanciation of the logger
logger = u.my_get_logger(path_log, log_level, my_name="main_logger")


def main(logger, step_list, NB_STEP_TOT, path_conf="../conf/conf.json"):
    """
    Main function launching step by step the ML Pipeline
    Args:
        logger: Logger file
        step_list: List of steps to be executes
        NB_STEP_TOT: By default = number of total step to laucnh them all if no specific steps are given
        path_conf: path of the conf file
    """
    START = time()

    # Computation of the steps to complete
    if len(step_list) > 0:
        step_list = eval(step_list)

    if (step == -1) and (len(step_list) == 0):
        step_list = list(range(step_from, NB_STEP_TOT + 1))

    print(step_list)
    logger.debug("Steps to execute :" + ", ".join(map(str, step_list)))

    # Reading conf file
    conf = json.load(open(path_conf, "r"))
    seed = 42

    # Launch of each selected step
    if (step == 1) or (1 in step_list):
        logger.debug("Beginning of step 1 - Loading and Preprocessing")
        # Reading of the dataset selected in the conf file
        df = loading.read_csv_from_name(conf)

        # Preprocessing of the selected dataset
        (
            df_preprocessed,
            X_columns,
            y_column,
            encoding_dict,
        ) = preprocessing.main_preprocessing_from_name(df, conf)

        # Writting of the preprocessed dataset
        loading.write_preprocessed_csv_from_name(
            df_preprocessed, conf, "data_preprocessed.csv"
        )

        # Writting the encoding dictionnary
        loading.write_dict_json_from_name(encoding_dict, conf, "encoding_dict.json")

        logger.debug("End of step 1 ")

    if (step == 2) or (2 in step_list):

        logger.debug(" Beginning of step 2 - Loading Preprocessed ")
        # Loading of the preprocessed dataset
        df_preprocessed = loading.load_preprocessed_csv_from_name(
            conf, "data_preprocessed.csv"
        )
        # Basic Splitting between train and test
        y_column = u.get_y_column_from_conf(conf)
        X_columns = [x for x in df_preprocessed.columns if x != y_column]
        # Basic Splitting between train and test
        X_train, X_test, y_train, y_test = preprocessing.basic_split(
            df_preprocessed, 0.25, X_columns, y_column
        )

        logger.debug(" End of step 2 ")

    if (step == 3) or (3 in step_list):
        if 2 not in step_list:  # Step 2 must be launched with step 3
            df_preprocessed = loading.load_preprocessed_csv_from_name(
                conf, "data_preprocessed.csv"
            )
            # Basic Splitting between train and test
            y_column = u.get_y_column_from_conf(conf)
            X_columns = [x for x in df_preprocessed.columns if x != y_column]
            X_train, X_test, y_train, y_test = preprocessing.basic_split(
                df_preprocessed, 0.25, X_columns, y_column, seed=seed
            )

        logger.debug(" Beginning of step 3 - Modeling ")

        # Modelisation using the model selected in the conf file
        clf, best_params = modeling.main_modeling_from_name(X_train, y_train, conf)
        # Saving the model
        u.save_model(clf, conf)
        logger.debug(" End of step 3 ")

    if (step == 4) or (4 in step_list):
        if 2 not in step_list:  # Step 2 must be launched with step 4
            df_preprocessed = loading.load_preprocessed_csv_from_name(
                conf, "data_preprocessed.csv"
            )
            # Basic Splitting between train and test
            y_column = u.get_y_column_from_conf(conf)
            X_columns = [x for x in df_preprocessed.columns if x != y_column]
            X_train, X_test, y_train, y_test = preprocessing.basic_split(
                df_preprocessed, 0.25, X_columns, y_column, seed=seed
            )

        logger.debug(" Beginning of step 4 - Evaluation")

        # Loading of the model
        clf = u.load_model(conf)

        # Computing metrics
        dict_metrics = evaluation.main_evaluation(clf, X_test, y_test, conf)

        logger.debug("End of step 4 ")

    if (step == 5) or (5 in step_list):
        if 2 not in step_list:  # Step 2 must be launched with step 5
            df_preprocessed = loading.load_preprocessed_csv_from_name(
                conf, "data_preprocessed.csv"
            )
            # Basic Splitting between train and test
            y_column = u.get_y_column_from_conf(conf)
            X_columns = [x for x in df_preprocessed.columns if x != y_column]
            X_train, X_test, y_train, y_test = preprocessing.basic_split(
                df_preprocessed, 0.25, X_columns, y_column, seed=seed
            )

        logger.debug(" Beginning of step 5 - Interpretability")

        # Loading of the model
        clf = u.load_model(conf)

        # Computing permutation importance
        interpretability.permutation_features_importance(conf, clf, X_train, y_train)

        # Computing the shap analysis
        shap_analysis = interpretability.shap_analysis(clf, X_test, y_test, conf)
        ## Variable Importance graphic
        shap_analysis.features_importance()
        ## Features importance + effect of the features according to their value
        shap_analysis.summary_plot()

        # Initialize the DICE class
        dice_interpretability = interpretability.dice_interpretability(
            clf, X_test, y_test, conf
        )
        ##Generate counterfactuals for a given input point
        dice_interpretability.global_interpretability(n=1000)

        logger.debug("End of step 5 ")

    logger.debug("Time for total execution :" + str(time() - START))


if __name__ == "__main__":
    try:
        main(logger, step_list, NB_STEP_TOT=4, path_conf=path_conf)

    except Exception as e:
        logger.error("Error during execution", exc_info=True)
