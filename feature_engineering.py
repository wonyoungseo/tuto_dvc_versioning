import os
import pandas as pd
from joblib import dump

from ml_src.data import preprocess

if __name__ == "__main__":

    train_df = pd.read_csv("./dataset/census_train.csv", sep='\t', encoding='utf-8')

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country"]

    label = "salary"

    X_train, y_train, encoder, lb = preprocess(train_df, categorical_features=cat_features, label=label, training=True)

    encoder_file_path = "./model/encoder.joblib"
    label_binarizer_file_path = "./model/lb.joblib"
    dump(encoder, encoder_file_path)
    dump(lb, label_binarizer_file_path)