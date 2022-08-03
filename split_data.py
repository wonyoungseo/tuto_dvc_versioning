import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":


    data = pd.read_csv("./dataset/census_cleaned.csv", sep='\t', encoding='utf-8')
    test_size = 0.2
    seed = 42

    train, test = train_test_split(data, test_size=test_size, random_state=seed)

    file_path = './dataset/census_{}.csv'
    train_file_path = file_path.format('train')
    test_file_path = file_path.format('test')

    train.to_csv(train_file_path, sep='\t', encoding='utf-8', index=False)
    test.to_csv(test_file_path, sep='\t', encoding='utf-8', index=False)