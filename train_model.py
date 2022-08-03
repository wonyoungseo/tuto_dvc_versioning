import json
import pandas as pd
from joblib import load, dump

from ml_src.data import preprocess
from ml_src.model import train_model, inference, compute_model_metrics

if __name__ == "__main__":
    train_df = pd.read_csv("./dataset/census_train.csv", sep='\t', encoding='utf-8')
    test_df = pd.read_csv("./dataset/census_test.csv", sep='\t', encoding='utf-8')

    encoder = load("./model/encoder.joblib")
    lb = load("./model/lb.joblib")

    with open("./model/model_parameters.json") as f:
        params = json.load(f)

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
    X_test, y_test, _, _ = preprocess(test_df, categorical_features=cat_features, label=label, training=False,encoder=encoder, lb=lb)

    model = train_model(X_train, y_train, params=params)

    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    model_performance = {
        "precision": precision,
        "recall": recall,
        "fbeta": fbeta
    }

    dump(model, "./model/model.joblib")
    with open("./model/model_performance.json", "w") as f:
        json.dump(model_performance, f)
