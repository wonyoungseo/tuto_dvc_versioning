```bash
# 1. init dvc
# Use  `--subdir` if initializing inside a subdirectory of a parent SCM repository.
dvc init --subdir

# 2. add remote storage (local path in this case)
dvc remote add -d myremote /tmp/dvcstore/

# 3. add data and commit to dvc
dvc add file
git add [file.dvc], [gitignore in file dir]
git commit -m "message"
dvc push

# 4. retrieve data
# 4.1. Getting data back from the `cache`
dvc checkout {data_dir}/{file_name}.dvc

# 4.2. Getting data in case the cache is empty
dvc fetch {data_dir}/{file_name}.dvc

# 4.3. Getting all data from DVC (not efficient)
dvc pull


# 5. model versioning
# 5.1. versioning each attempt
dvc add [model generated files]
git add [model generated files].dvc
git commit -m "message"
git tag -a "version alias : v1.0" -m "version message"
dvc push

# 5.2. versioning each attempt
# switching model version
git checkout [version alias]
dvc checkout
```



```bash
dvc init --subdir
dvc remote add -d myremote /tmp/dvcstore/

cd dataset
dvc add census_raw.csv
git add .gitignore census_raw.csv.dvc
git commit -m "add raw dataset."
dvc push
cd ..

python clean_data.py 
dvc add dataset/census_cleaned.csv 
git add dataset/census_cleaned.csv.dvc dataset/.gitignore
dvc push

python split_data.py 
dvc add dataset/census_train.csv dataset/census_test.csv
git add dataset/census_train.csv.dvc dataset/census_test.csv.dvc dataset/.gitignore
git commit -m "add splitted dataset."
dvc push

python feature_engineering.py
dvc add model/encoder.joblib model/lb.joblib
git add model/encoder.joblib.dvc model/lb.joblib.dvc model/.gitignore
git commit -m "add artifacts for feature engineering."
dvc push

python train_model.py
dvc add model/model_parameters.json model/model.joblib model/model_performance.json
git add model/model.joblib.dvc model/model_performance.json.dvc model/model_parameters.json.dvc model/.gitignore
git commit -m "v1.0 - model 1st attempt"
git tag -a "v1.0" -m "model v1.0"
dvc push

# after change some params
python train_model.py
dvc add model/model_parameters.json model/model.joblib model/model_performance.json
git add model/model.joblib.dvc model/model_performance.json.dvc model/model_parameters.json.dvc model/.gitignore
git commit -m "v2.0 - model 2nd attempt"
git tag -a "v2.0" -m "model v2.0"
dvc push
```