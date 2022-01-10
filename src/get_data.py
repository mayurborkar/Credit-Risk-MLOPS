# Read Params
# Process It
# Return DataFrame

import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
        #print(config)
    return config


def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    df.drop(["Unnamed: 0", "other_debtors", "other_installment_plans", "housing", "job", "people_liable",
             "foreign_worker"], axis=1, inplace=True)
    # print(df.head())
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('--config', default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
