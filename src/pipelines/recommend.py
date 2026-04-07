import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from dataset_cleaned.df_reader import load_df
from rapidfuzz import process

# Load the preprocessed data
df_new = load_df("output.csv")

# Vectorize the tags
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
feature_vectors = cv.fit_transform(df_new['tags'])

# Calculate cosine similarity
similarity = cosine_similarity(feature_vectors)

# Get movie names list
movie_names = df_new['clean_title'].tolist()

def recommend(movie_title, top_n=10):
    """
    Recommend similar movies based on content-based filtering.
    
    Parameters:
    - movie_title: Title of the movie to find recommendations for
    - top_n: Number of recommendations to return
    
    Returns:
    - List of recommended movie titles
    """
    # Find closest match using rapidfuzz
    find_close_match = process.extract(movie_title, movie_names, limit=5)
    
    if not find_close_match:
        return []
    
    # Get the closest match
    closest_match_title = find_close_match[0][0]
    
    # Find index of the movie
    try:
        index_of_the_movie = df_new[df_new["clean_title"] == closest_match_title].index[0]
    except IndexError:
        return []
    
    # Get similarity scores
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    
    # Sort by similarity score in descending order
    sorted_similar_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    
    # Get top N recommendations (excluding the input movie)
    recommended_titles = []
    count = 0
    for i in sorted_similar_score:
        if i[0] == index_of_the_movie:
            continue  # skip same movie
        
        recommended_titles.append(df_new.iloc[i[0]]['title'])
        count += 1
        
        if count >= top_n:
            break
    
    return recommended_titles

# Example usage
if __name__ == "__main__":
    movie_title = "ironman"
    recommendations = recommend(movie_title)
    print(f"Recommendations for '{movie_title}':")
    for i, title in enumerate(recommendations, 1):
        print(f"{i}. {title}")