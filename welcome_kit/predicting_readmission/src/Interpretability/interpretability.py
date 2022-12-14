# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('main_logger')

import dice_ml
from dice_ml import Dice
import pandas as pd
from random import randint
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import shap 
from sklearn.inspection import permutation_importance
from tqdm.auto import tqdm

#This script implement several interpretability tools 
#You can find Permutation Importance, SHAP and DICE

####### Permutation Importance ########

def permutation_features_importance(conf, model, X_train, y_train, n_repeats=10):
    """
    Calculate and return the features importance by permutation

    Args:
        conf : Conf file
        model : The model to evaluate
        X_train : dataset
        y_train : target
        n_repeats (int, optional): Number of permutation. Defaults to 10.

    Returns:
        Dict file with the value as well as a graph
    """
    feature_importances = permutation_importance(
        model, X_train, y_train, n_repeats=n_repeats
    )

    sorted_idx = feature_importances.importances_mean.argsort()

    plt.figure(figsize=(12,8)) 
    plt.title("Permutation Importances")
    plt.boxplot(feature_importances.importances[sorted_idx].T,
            vert=False, labels=X_train.columns[sorted_idx])
    plt.savefig(conf['Outputs_path'] + conf['folder_interpretability'] + 'permutation_'
              + conf['selected_dataset'] + "_" + conf['selected_model'] + 
              '_features_importance.png')
    dict_importance = dict(zip(X_train.columns[sorted_idx], feature_importances.importances[sorted_idx].T.mean(axis=0))) 

    return dict_importance


####### SHAP ########

class shap_analysis :
    """
    Class with all the different shap tools
    """
    def __init__(self, model, X, y, conf):
        self.conf = conf
        self.model = model
        self.X = X
        self.y = y.values
        self.feature_names = X.columns
        logger.info('Beginning of calculating the SHAP values using ' + conf['selected_model'])
        self.explainer = shap.TreeExplainer(model)
        self.shap_values = self.explainer.shap_values(X)
        logger.info('End of calculating the SHAP values using ' + conf['selected_model'])

    def features_importance(self):
        """
        Return the shapley values feature importance
        """
        conf = self.conf
        plt.title("Most important features for the " + conf['selected_dataset'] + " " + 
            conf['selected_model'] + " model", size=15)
        shap.summary_plot(self.shap_values[1], self.X, 
            plot_type="bar", feature_names = self.feature_names)
        plt.savefig(conf['Outputs_path'] + conf['folder_interpretability'] + 'shap_'
              + conf['selected_dataset'] + "_" + conf['selected_model'] + 
              '_features_importance.png')

    def summary_plot(self):
        """
        Return the summary plot
        """
        conf = self.conf
        plt.title("Summary plot for the " + conf['selected_dataset'] + " " + 
            conf['selected_model'] + " model", size=15)
        shap.summary_plot(self.shap_values[1], self.X, self.feature_names)
        plt.savefig(conf['Outputs_path'] + conf['folder_interpretability'] + 'shap_'
              + conf['selected_dataset'] + "_" + conf['selected_model'] + 
              '_summary_plot.png')

    def global_force_plot(self, n='max'):
        """
        Return the global Force plot
        """
        if n=='max':
            n = len(self.X)
        shap.initjs()
        p = shap.force_plot(self.explainer.expected_value[1], self.shap_values[1][:n], self.X, 
            feature_names=self.feature_names)
        return p

    def local_force_plot(self, i='random'):
        """
        Return the local force plot. If no point is given it takes a random points.
        """
        if i == 'random' :
            i = randint(0, len(self.X)-1)
        y_result_test = self.model.predict(self.X)

        print("For the", i,"th value the predicted value of y is", y_result_test[i],
            ". Nevertheless, the true value of y is", self.y[i])

        shap.initjs()
        p = shap.force_plot(self.explainer.expected_value[1], self.shap_values[1][i,:], 
            self.X.iloc[i,:],feature_names=self.feature_names)
        return p

    def cat_features_explanability(self, var, encoding_dict):
        """
        Return the shapley effect for each category of a given variable
        """
        k = list(self.feature_names.values).index(var)
        shap_var_importance = self.X[[var]]
        shap_var_importance['shap_value'] = self.shap_values[1][:, k]
        shap_var_importance = shap_var_importance.reset_index(drop=True)
        shap_var_importance = shap_var_importance.replace({var:  {v: k for k, v in encoding_dict[var].items()}})

        my_order = shap_var_importance.groupby(by=[var])['shap_value'].mean().index
        plt.title(var + ' local shap effect')
        sns.boxplot(y='shap_value', x=var, data=shap_var_importance, order=my_order, showmeans=True,
             meanprops={"marker": "o",
                       "markerfacecolor": "white", 
                       "markeredgecolor": "red",
                       "markersize": "8"})
        plt.savefig(self.conf['Outputs_path'] + self.conf['folder_interpretability'] + 'shap_'
              + self.conf['selected_dataset'] + "_" + self.conf['selected_model'] + '_' + var + '_importance.png')

        return shap_var_importance


        


####### DICE ########

class dice_interpretability():
    """
    Counterfactual analysis of a model with dice library
    """
    def __init__(self, model, X, y, conf, backend="sklearn", method="random", continuous_features=[]):
        self.conf = conf
        self.X = X.copy()
        self.dataset = X.copy()
        self.dataset['target'] = y

        
        #Define a Dice Datset
        d = dice_ml.Data(dataframe=self.dataset, continuous_features=continuous_features, 
            outcome_name='target')
        #Define a Dice Model
        m = dice_ml.Model(model=model, backend=backend)
        #Perform the counterfactual analysis with Dice
        self.exp = Dice(d, m, method=method)

    def local_interpretability(self, instance='random', total_CFs=4):
        """
        Analyse just on one row
        """
        # Choose a random sample if not indicate
        if instance == 'random':
            query_instance = self.X.sample(1)
        else :
            query_instance = self.X[instance:instance+1]

        e1 = self.exp.generate_counterfactuals(query_instance, total_CFs=total_CFs, desired_range=None,
                                    desired_class="opposite",
                                    permitted_range=None, features_to_vary='all',
                                    verbose=False)
        e1.visualize_as_dataframe(show_only_changes=True)
        return e1

    def global_interpretability(self, n='max'):
        """
        Calculate the  Necessity for all the variable according to a sample n of data
        """
        conf = self.conf
        if n=='max':
            n = len(self.X)
        #For necessity, we need to generate counterfactuals for a representative sample of the dataset.
        logger.info('Beginning of calculating the Necessity values using ' + conf['selected_model'])
        cobj = self.exp.global_feature_importance(self.X.sample(n), 
            total_CFs=10, posthoc_sparsity_param=None)
        #Convert the result to a dict
        gloabl_inter = cobj.summary_importance 
        logger.info('End of calculating the Necessity values using ' + conf['selected_model'])

        keys = list(gloabl_inter.keys())
        values = list(gloabl_inter.values())

        plt.title("Dice features importance" + conf['selected_dataset'] + " " + 
            conf['selected_model'] + " model", size=15)
        plt.barh(keys[::-1], values[::-1])
        plt.savefig(conf['Outputs_path'] + conf['folder_interpretability'] + 'dice_'
              + conf['selected_dataset'] + "_" + conf['selected_model'] + 
              '_features_importance.png')

        return gloabl_inter

    def sufficency(self, var, n='max', total_CFs=4):
        """
        Calculate the  Sufficency for one variable according to a sample n of data
        """
        if n=='max':
            n = len(self.X)
        #initialise several features
        sufficency = 0
        features_to_vary = list(self.X.columns)
        features_to_vary.remove(var)
        #Randomize the process
        df = self.X.sample(n)
        logger.info('Beginning of calculating the Sufficency values using ' + self.conf['selected_model'] + ' for the features: ' + var)
        for k in tqdm(range(n)):
            query_instance = df[k:k+1]
            original_value = query_instance[var].values[0]
            #Calculate the counterfactual without the variables
            e1 = self.exp.generate_counterfactuals(query_instance, total_CFs=total_CFs, desired_range=None,
                                            desired_class="opposite",
                                            permitted_range=None, features_to_vary=features_to_vary, verbose=False)
            #Calculate the counterfactual for all variables
            e2 = self.exp.generate_counterfactuals(query_instance, total_CFs=total_CFs, desired_range=None,
                                            desired_class="opposite",
                                            permitted_range=None, features_to_vary='all', verbose=False)
            # Calculate the difference between the counterfactual created with and without the variables
            sufficency += len(e2.cf_examples_list[0].final_cfs_df_sparse) - len(e1.cf_examples_list[0].final_cfs_df_sparse)

        sufficency = sufficency / (n*total_CFs)
        logger.info('End of calculating the Sufficency values using ' + self.conf['selected_model'] + ' for the features: ' + var)
        logger.info('Sufficency of ' + var + ' is equal to : ' + sufficency)
        return_dict = {
            var: sufficency
        }

        return return_dict