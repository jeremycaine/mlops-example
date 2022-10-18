import os
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = os.getenv('PATH')
print(PATH)

#LOC_TRAIN_CSV = 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-dataset/mnist_train.csv' 
#LOC_TEST_CSV = 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-dataset/mnist_test.csv'
#LOC_MODEL = 'https://s3.us-east.cloud-object-storage.appdomain.cloud/caine-mnist-model/cities.csv'

LOC_TRAIN_CSV = os.get('LOC_TRAIN_CSV')
LOC_TEST_CSV = os.get('LOC_TEST_CSV')
LOC_MODEL = os.get('LOC_MODEL')

COS_IAM_KEY = os.get('CLOUD_OBJECT_STORAGE_APIKEY')
print(COS_IAM_KEY)
# -- Build the model
# train_df: pd.DataFrame = pd.read_csv(LOC_TRAIN_CSV, header=None)
test_df: pd.DataFrame = pd.read_csv(LOC_TEST_CSV, header=None)

data: test_df.loc[1:, 1:2].values
print(data)

cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
x = cities.to_csv(index=False)
print(x)

print("data loaded")
