# -*- coding: utf-8 -*-
'''
# Model Evaluation Tools
# 
# This is set of utilities to evaluate sentiment models
# most of this code came from Dipanjan Sarkar (from his book).
#
# I've merely recoded it in order to learn the inner workings
# of how the models are evaluated, and commented them.
#
# Reference: Practical Machine Learning with Python by Dipanjan Sarkar
#
# Metrics/Training
#   - get_metrics()
# 
# Display Functions
#   - display_confusion_matrix()
#   - display_classification_report()
#   - display_model_performance_metrics()
#
#
'''

import numpy as np
import pandas as pd
from scipy import interp
import matplotlib.pyplot as plt


from sklearn import metrics
from sklearn.base import clone
from sklearn.preprocessing import LabelEncoder, label_binarize
from sklearn.metrics import roc_curve, auc

# display_model_performance_metrics()
def display_model_performance_metrics(labels, predicted_labels, classes=[1, 0]):
    print("MODEL PERFORMANCE METRICS")
    print('*' * 40)
    get_metrics(labels=labels, predicted_labels=predicted_labels)

    print("\nMODEL CLASSIFICATION REPORT")
    print('*' * 40)
    display_classification_report(labels=labels, predicted_labels=predicted_labels, classes=classes)
    
    print("\nCONFUSION MATRIX FOR PREDICTIONS")
    print('*' * 40)
    display_confusion_matrix(labels=labels, predicted_labels=predicted_labels, classes=classes)

# get_metrics() prints out the Accuracy, Precision, Recall and F1 Score
def get_metrics(labels, predicted_labels):
    accuracy = np.round(metrics.accuracy_score(labels, predicted_labels), 4)
    precision = np.round(metrics.precision_score(labels, predicted_labels, average='weighted'), 4)
    recall = np.round(metrics.recall_score(labels, predicted_labels, average='weighted'), 4)
    f1_score = np.round(metrics.f1_score(labels, predicted_labels, average='weighted'), 4)

    # Display
    print("Accuracy: " + accuracy)
    print("Precision: " + precision)
    print("Recall: " + recall)
    print("F1 Score: " + f1_score)

def display_classification_report(labels, predicted_labels, classes=[1, 0]):
    report = metrics.classification_report(y_true=labels, y_pred=predicted_labels, labels=classes)
    print(report)

def display_confusion_matrix(labels, predicted_labels, classes=[1, 0]):
    tc = len(classes)
    ll = [lc*[0], list(range(tc))]
    cm = metrics.confusion_matrix(y_true=labels, y_pred=predicted_labels, labels=classes)
    cm_display = pd.DataFrame(data=cm, columns=pd.MultiIndex(levels=[['Predicted: '], classes], labels=ll), 
                              index=pd.MultiIndex(levels=[['Actual: '], classes], labels=ll))
    print(cm_display)
