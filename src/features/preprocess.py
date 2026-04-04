# Preprocessing code comes Here
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from src.data.loader import df

def preprocess(x):
    L = []
    for i in x:
        L.append(i["name"])
    return L

def preprocess_cast(x):
    L = []
    for i in x[:3]:
        L.append(i["name"])
    return L

# preprocess(json.loads(df.iloc[0]['genres']))
df['genres'] = df['genres'].apply(json.loads).apply(preprocess)
df['keywords'] = df['keywords'].apply(json.loads).apply(preprocess)
df['cast'] = df['cast'].apply(json.loads).apply(preprocess_cast)
df['crew'] = df['crew'].apply(json.loads).apply(lambda x: [i['name'] for i in x if i['job'] == 'Director'])
df['genres'] = df['genres'].apply(lambda x: [i.replace(" ","") for i in x])
df['keywords'] = df['keywords'].apply(lambda x: [i.replace(" ","") for i in x])
df['cast'] = df['cast'].apply(lambda x: [i.replace(" ","") for i in x])
df['crew'] = df['crew'].apply(lambda x: [i.replace(" ","")  for i in x])

# Combining all the 5 selected features
combined_string = (
    df['overview'] * 1 + " " +
    df['genres'].apply(lambda x: " ".join(x)) * 3 + " " +
    df['keywords'].apply(lambda x: " ".join(x)) * 2 + " " +
    df['cast'].apply(lambda x: " ".join(x)) * 2 + " " +
    df['crew'].apply(lambda x: " ".join(x)) * 2
)

df['tags'] = combined_string.apply(lambda x: x.lower())

df_new = df[['movie_id','title','tags']]

df_new['clean_title'] = (
    df_new['title']
    .astype(str)
    .str.lower()
    .str.replace(r'[^a-z0-9]', '', regex=True)
)

df_new.to_csv("../dataset_cleaned/output.csv", index=False)

print(df.head())