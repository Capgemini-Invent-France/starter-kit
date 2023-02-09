# -*- coding: utf-8 -*-
import logging
import pickle

logger = logging.getLogger("main_logger")


def my_get_logger(path_log, log_level, my_name=""):
    """
    Instanciation du logger et paramétrisation
    :param path_log: chemin du fichier de log
    :param log_level: Niveau du log
    :return: Fichier de log
    """

    # print(path_log)
    # print(log_level)

    log_level_dict = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }

    LOG_LEVEL = log_level_dict[log_level]
    # print(LOG_LEVEL)

    if my_name != "":
        logger = logging.getLogger(my_name)
        logger.setLevel(LOG_LEVEL)
    else:
        logger = logging.getLogger(__name__)
        logger.setLevel(LOG_LEVEL)

    # create a file handler
    handler = logging.FileHandler(path_log)
    handler.setLevel(LOG_LEVEL)

    # create a logging format
    formatter = logging.Formatter(
        "%(asctime)s - %(funcName)s - %(levelname)-8s: %(message)s"
    )
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    return logger


def save_model(clf, conf, name=""):
    if len(name) == 0:
        name = conf["selected_dataset"] + "_" + conf["selected_model"]
    filename = conf["Outputs_path"] + conf["folder_models"] + name + ".sav"
    pickle.dump(clf, open(filename, "wb"))
    logger.info("Modele sauvergarde: " + filename)
    return "OK"


def load_model(conf, name=""):
    if len(name) == 0:
        name = conf["selected_dataset"] + "_" + conf["selected_model"]
    filename = conf["Outputs_path"] + conf["folder_models"] + name + ".sav"
    print(filename)
    clf = pickle.load(open(filename, "rb"))
    logger.info("Modele charge: " + filename)
    return clf


def get_y_column_from_conf(conf):

    if conf["selected_dataset"] == "diabetic":
        y = "readmitted"
    else:
        logger.error("This dataset do no have any y column or do not exist")

    return y
