import os
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -- Build the model
# train_df: pd.DataFrame = pd.read_csv('Resources/mnist_train.csv', header=None)
test_df: pd.DataFrame = pd.read_csv('https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-dataset/mnist_test.csv', header=None)

data: test_df.loc[1:, 1:2].values

cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv('https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-model/cities.csv')

print(data)
print("data loaded")
