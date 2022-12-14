# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('main_logger')

from sklearn.model_selection import KFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Description of this script:
# Implement a cross validation (function) to check the robustness of a parameter set
# Implement on it a grid search to select the best parameter set
# Implementseveral models



def main_modeling_from_name (X_train, y_train, conf):
    """
    Main modeling function: it launches a grid search using the correct model according to the conf file
    Args:
        X_train: X_train
        y_train: y_train
        conf: configuration file

    Returns: model fitted on the train set and its best params

    """

    dict_function_GS_params = {'random_forest': 'get_GS_params_RFClassifier',
                                'ADABoost': 'get_GS_params_AdaBoost',
                                'xg_boost': 'get_GS_params_xgboost',
                                'logistic_regression': 'get_GS_params_logistic',
                                'KNeighbors': 'get_GS_params_kneighbors'}
    dict_function_train_model = {'random_forest': 'train_RFClassifier',
                                'ADABoost': 'train_AdaBoost',
                                'xg_boost': 'train_xgboost',
                                'logistic_regression': 'train_logistic',
                                'KNeighbors': 'train_kneighbors'}

    selected_model = conf['selected_model']
    function_get_GS_params = globals()[dict_function_GS_params[selected_model]]
    estimator, params_grid = function_get_GS_params()

    logger.info('Beginning of Grid Search using ' + selected_model)
    best_params, best_score = main_GS_from_estimator_and_params(X_train, y_train, estimator, params_grid, conf)

    function_train = globals()[dict_function_train_model[selected_model]]
    model = function_train(X_train,y_train, best_params)
    logger.info('End of Grid Search using ' + selected_model)
    logger.info('Best parameteres are :')
    logger.info(best_params)
    logger.info('best score' + str(best_score))

    return model, best_params


def main_GS_from_estimator_and_params(X_train, y_train, estimator, params_grid, conf):
    """
    Main function to run a grid search
    Args:
        X_train: X_train
        y_train:  y_train
        estimator: unfit model to use
        params_grid: grid search to run
        conf: conf file

    Returns: best params and score achieved in the GS

    """
    gkf = KFold(n_splits=5, shuffle=True, random_state=42).split(X=X_train, y=y_train)


    gsearch = GridSearchCV(estimator=estimator, param_grid=params_grid, cv=gkf,
                           scoring=conf['scoring'], verbose=1, n_jobs = -1)
    best_model = gsearch.fit(X=X_train, y=y_train)

    return best_model.best_params_, best_model.best_score_


####### RANDOM FOREST  ########
def get_GS_params_RFClassifier():
    """
    Gives params and models to use for the grid_search using Random Forest Classifier
    Returns:Estimator and params for the grid_search
    """
    params_grid = {
              'n_estimators': [50, 100, 150, 200], 
              'max_depth': [None], 
              'max_features': ['auto'],
              'min_samples_split': [5, 10, 15, 20],
              'min_samples_leaf': [1, 2, 4]
              }
    estimator = RandomForestClassifier()

    return estimator, params_grid

def train_RFClassifier(X_train,y_train,params):
    """
    Training function for a Random Forest Classifier
    Args:
        X_train: 
        y_train: 
        params: params to use for the fitting

    Returns: trained random forest model

    """
    model = RandomForestClassifier(**params).fit(X_train,y_train)
    return model


####### XG Boost  ########
def get_GS_params_xgboost():
    """
    Gives params and models to use for the grid_search using XG-Boost
    Returns:Estimator and params for the grid_search
    """
    params_grid = {
              'learning_rate': [0.05, 0.1, 0.15], 
              'max_depth': [2, 3, 4],
              'early_stopping_rounds': [3, 5], 
              'n_estimators': [100, 150, 200],
              'min_child_weight': [1, 3]
        }
    estimator = XGBClassifier(objective='binary:logistic', silent=True)

    return estimator, params_grid

def train_xgboost(X_train,y_train,params):
    """
    Training function for a XG-Boost model
    Args:
        X_train: 
        y_train: 
        params: params to use for the fitting

    Returns: trained random forest model

    """
    model = XGBClassifier(**params).fit(X_train,y_train)
    return model


####### Logistic Regression  ########
def get_GS_params_logistic():
    """
    Gives params and models to use for the grid_search using Logistic Regression
    Returns:Estimator and params for the grid_search
    """
    params_grid = {
              'penalty': ["l1","l2"],
              'multi_class': ["auto", "ovr", "multinomial"],
              'C': np.logspace(-3,3,7)
        }
    estimator = LogisticRegression()

    return estimator, params_grid

def train_logistic(X_train, y_train, params):
    """
    Training function for a Logistic Regression model
    Args:
        X_train: 
        y_train: 
        params: params to use for the fitting

    Returns: trained random forest model

    """
    model = LogisticRegression(**params).fit(X_train,y_train)
    return model


####### KNeighbors  ########
def get_GS_params_kneighbors():
    """
    Gives params and models to use for the grid_search using KNeighbors
    Returns:Estimator and params for the grid_search
    """
    params_grid = {
              'n_neighbors': [3, 5, 7, 10],
              'weights': ["uniform", "distance"],
              'algorithm': ["auto", "ball_tree", "kd_tree", "brute"],
              'p': [1, 2]
        }
    estimator = KNeighborsClassifier()

    return estimator, params_grid

def train_kneighbors(X_train, y_train, params):
    """
    Training function for a KNeighbors model
    Args:
        X_train: 
        y_train: 
        params: params to use for the fitting

    Returns: trained random forest model

    """
    model = KNeighborsClassifier(**params).fit(X_train,y_train)
    return model

####### ADA Boost  ########
def get_GS_params_AdaBoost():
    """
    Gives params and models to use for the grid_search using ADA Boost
    Returns:Estimator and params for the grid_search
    """
    params_grid = {
              'base_estimator__max_depth': [i for i in range(2, 11, 2)],
              'base_estimator__min_samples_leaf': [5, 10],
              'n_estimators': [10, 50, 250, 1000],
              'learning_rate': [0.01, 0.1]
        }
    DTC = DecisionTreeClassifier(max_features="auto", class_weight="auto", max_depth=None)
    estimator = AdaBoostClassifier(base_estimator=DTC)

    return estimator, params_grid

def train_AdaBoost(X_train, y_train, params):
    """
    Training function for a ADA Boost model
    Args:
        X_train: 
        y_train: 
        params: params to use for the fitting

    Returns: trained random forest model

    """
    model = AdaBoostClassifier(**params).fit(X_train,y_train)
    return model