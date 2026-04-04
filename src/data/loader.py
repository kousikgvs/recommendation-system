# Loader code comes Here

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# loading the data from a CSV file to pandas data
df1 = pd.read_csv("C:\\Users\\kousi\\Documents\\recommendation-system\\dataset\\tmdb_5000_credits.csv")

# loading the data from a CSV file to pandas data
df2 = pd.read_csv("C:\\Users\\kousi\\Documents\\recommendation-system\\dataset\\tmdb_5000_movies.csv")

df = df1.merge(df2 , on="title" , how='inner')

selected_features = ['movie_id' , 'title','overview' , 'genres','keywords','cast','crew']


