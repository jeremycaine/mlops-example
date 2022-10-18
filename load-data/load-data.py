import os
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LOC_TRAIN_CSV = 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-dataset/mnist_train.csv' 
LOC_TEST_CSV = 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-dataset/mnist_test.csv'
LOC_MODEL = 'https://s3.us-east.cloud-object-storage.appdomain.cloud/caine-mnist-model/cities.csv'

# -- Build the model
# train_df: pd.DataFrame = pd.read_csv(LOC_TRAIN_CSV, header=None)
test_df: pd.DataFrame = pd.read_csv(LOC_TEST_CSV, header=None)

data: test_df.loc[1:, 1:2].values

cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv(LOC_MODEL)

print(data)
print("data loaded")
