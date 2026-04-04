# Loader code comes Here

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dataset.df_reader import df1, df2

# loading the data from a CSV file to pandas data

df = df1.merge(df2 , on="title" , how='inner')

selected_features = ['movie_id' , 'title','overview' , 'genres','keywords','cast','crew']
