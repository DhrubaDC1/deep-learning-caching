#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import dask.dataframe as dd

#importing datasets
dataset_movies = pd.read_csv('movies.csv')
dataset_rating = pd.read_csv('ratings.csv')
x_movies = dataset_movies.iloc[:, :-1].values
y_movies = dataset_movies.iloc[:, 2].values
x_rating = dataset_rating.iloc[:, :-1].values
y_rating = dataset_rating.iloc[:, 3].values

#Converting genres into catagory
from sklearn.preprocessing import LabelEncoder
labelencoder_y_movies = LabelEncoder()
y_movies[:] = labelencoder_y_movies.fit_transform(y_movies[:])

#timestamp to timestamp_hour, timestamp_day, timestamp_year
df = np.ceil(pd.DataFrame(y_rating, columns=['timestamp_day'])/86400)
df = df.to_numpy()
# df = np.append(y_rating, df)