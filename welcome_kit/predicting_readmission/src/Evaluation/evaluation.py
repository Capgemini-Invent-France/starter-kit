# -*- coding: utf-8 -*-
# author :pierre_lavieille

import logging

logger = logging.getLogger("main_logger")

from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import recall_score, precision_score, roc_auc_score, roc_curve
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import json

# Description of this script:
# This script calculate several metrics from the model and the test set


def main_evaluation(clf, X_test, y_test, conf):
    """
    Main Evaluation Function: computes metrics and save them into a json file
    Args:
        clf: model used for the metricsyy
        X_test: X_test
        y_test: y_test
        conf:  Conf File

    Returns: Dict of metrics and saves the metrics into a json file

    """

    y_test_pred = clf.predict(X_test)
    y_test_prob = clf.predict_proba(X_test)[:, 1]

    dict_metrics = {}
    dict_metrics["f1_score"] = metric_f1_score(y_test, y_test_pred)
    dict_metrics["accuracy"] = metric_accuracy(y_test, y_test_pred)
    dict_metrics["roc_accuracy"] = roc_auc_score(
        y_test, clf.predict_proba(X_test)[:, 1]
    )
    dict_metrics["recall"] = metric_recall(y_test, y_test_pred)
    dict_metrics["precision"] = metric_precision(y_test, y_test_pred)
    dict_metrics["confusion_matrix"] = metric_confusion_matrix(y_test, y_test_pred)

    with open(
        conf["Outputs_path"]
        + conf["folder_metrics"]
        + "metrics_"
        + conf["selected_dataset"]
        + "_"
        + conf["selected_model"]
        + "_classifier.txt",
        "w",
    ) as outfile:
        json.dump(str(dict_metrics), outfile)

    # Calculate the sklearn coufusion matrix
    cm = confusion_matrix(y_test, y_test_pred)
    # Display this confusion matrix
    plt.figure(figsize=(12, 8))
    plt.title("Confusion Matrix")
    sns.heatmap(np.round(cm / cm.sum(axis=1)[:, None], 3), annot=True)
    plt.savefig(
        conf["Outputs_path"]
        + conf["folder_metrics"]
        + "metrics_"
        + conf["selected_dataset"]
        + "_"
        + conf["selected_model"]
        + "_confusions_matrix.png"
    )

    # Calculate roc curves
    ns_probs = [0 for _ in range(len(y_test))]
    ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
    lr_fpr, lr_tpr, _ = roc_curve(y_test, y_test_prob)

    # Plot the roc curve for the model
    plt.figure(figsize=(12, 8))
    plt.plot(ns_fpr, ns_tpr, linestyle="--", label="No Skill")
    plt.plot(lr_fpr, lr_tpr, marker=".", label="model")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.savefig(
        conf["Outputs_path"]
        + conf["folder_metrics"]
        + "metrics_"
        + conf["selected_dataset"]
        + "_"
        + conf["selected_model"]
        + "_roc_curve.png"
    )
    plt.show()
    return dict_metrics


def metric_f1_score(y_true, y_pred):
    return roc_auc_score(y_true, y_pred)


def metric_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)


def metric_roc_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)


def metric_recall(y_true, y_pred):
    return recall_score(y_true, y_pred)


def metric_precision(y_true, y_pred):
    return precision_score(y_true, y_pred)


def metric_confusion_matrix(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    dict_confusion_matrix = {"tn": tn, "fp": fp, "fn": fn, "tp": tp}
    return dict_confusion_matrix
