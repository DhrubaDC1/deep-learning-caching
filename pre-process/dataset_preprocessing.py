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

#using regEx for extracting release date from title
temp_rd = dataset_movies['title'].str.extract('(\(\d.{3})',expand=False)
dataset_movies['releaseDate'] = temp_rd.str.extract('(\d+)',expand=False)

#timestamp to timestamp_hour, timestamp_day, timestamp_year
dataset_rating['timestamp_hour'] = np.ceil(y_rating/3600)
dataset_rating['timestamp_day'] = np.ceil(y_rating/86400)
dataset_rating['timestamp_year'] = np.ceil(y_rating/31536000)

#merge datasets
merged = pd.merge(dataset_movies, dataset_rating, on = 'movieId')

#save merged as csv
merged.to_csv('joined.csv')

#preprocessing
labelencoder_timestamp_day = LabelEncoder()
cat = labelencoder_timestamp_day.fit_transform(merged['timestamp_day'])











