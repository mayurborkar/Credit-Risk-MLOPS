from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from get_data import read_params
import pandas as pd
import numpy as np
import argparse
import warnings
import joblib
import json
import sys
import os


def eval_metrics(actual, pred):
    accuracy = accuracy_score(actual, pred)
    precision = precision_score(actual, pred)
    recall = recall_score(actual, pred)
    roc_auc = roc_auc_score(actual, pred)
    return accuracy, precision, recall, roc_auc


def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    max_depth = config["estimators"]["RandomForestClassifier"]["params"]["max_depth"]
    max_features = config["estimators"]["RandomForestClassifier"]["params"]["max_features"]
    n_estimators = config["estimators"]["RandomForestClassifier"]["params"]["n_estimators"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    rfc = RandomForestClassifier(max_depth=max_depth,
                                 max_features=max_features,
                                 n_estimators=n_estimators,
                                 random_state=random_state)
    rfc.fit(train_x, train_y)

    predicted_qualities = rfc.predict(test_x)

    (accuracy, precision, recall, roc_auc) = eval_metrics(test_y, predicted_qualities)

    print("Random Forest Classifier Model (max_depth=%f, max_features=%f, n_estimators=%f):" % (max_depth,
                                                                                                max_features,
                                                                                                n_estimators))
    print("Accuracy: %s" % accuracy)
    print("Precision: %s" % precision)
    print("Recall: %s" % recall)
    print("Roc_Auc_Score: %s" % roc_auc)

    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "accuracy" : accuracy,
            "precision" : precision,
            "recall" : recall,
            "roc_auc" : roc_auc
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        scores = {
            "max_depth": max_depth,
            "max_features": max_features,
            "n_estimators": n_estimators
        }
        json.dump(scores, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(rfc, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
