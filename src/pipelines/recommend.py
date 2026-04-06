# Recommendation pipeline code comes Here

# Preprocessing code comes Here
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from dataset_cleaned.df_reader import df_new

# # Converting all the Text Data to Numbering vectors
# vectorizer = TfidfVectorizer()
# feature_vectors = vectorizer.fit_transform(df_new['clean_title'] + ' ' + df_new['tags'])

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000 , stop_words='english')
feature_vectors = cv.fit_transform(df_new['tags'])
feature_vectors.shape

