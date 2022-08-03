import pandas as pd


if __name__ == "__main__":


    data = pd.read_csv("./dataset/census_raw.csv", sep=',', encoding='utf-8')

    # cleaning column name, data
    data.columns = [c.strip() for c in data.columns]

    for col in data.columns:
        if data[col].dtype == 'O':
            data[col] = data[col].apply(lambda x: x.strip())

    # convert ? to NA
    data.replace({"?": None}, inplace=True)

    # drop values that contains "?"
    data.dropna(inplace=True)

    # drop irrelevant value
    data.drop(columns="fnlgt", inplace=True)

    # drop highly correlated numerical feature
    data.drop(columns=["education-num"], inplace=True)

    # drop features with mostly zero
    data.drop(columns=["age", "capital-gain", "capital-loss"], inplace=True)

    # overwrite
    data.to_csv('./dataset/census_cleaned.csv', sep='\t', encoding='utf-8', index=False)