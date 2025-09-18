import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


# Load the CSV
df = pd.read_csv('Week-03-EDA-and-Dashboards/data/movie_ratings.csv')
df.info()
df = df.dropna()
df = df.drop_duplicates()

#Title
st.title("Movie Genres Dashboard 🎬")


#Question 1:
st.caption("Question 1: What's the breakdown of genres for the movies that were rated?")


# Count genres (assuming single genre per movie)
genre_counts = df['genres'].value_counts()
genre_counts = genre_counts.sort_values(ascending=False)

st.bar_chart(genre_counts, horizontal=True)


#Question 2:

st.caption("2. Which genres have the highest viewer satisfaction (highest ratings)? ")

genres_by_ratings = df.groupby('genres')['rating'].mean().sort_values(ascending= False)


st.bar_chart(genres_by_ratings, use_container_width=True)


#Question 3:

st.caption("3.How does mean rating change across movie release years?")

rating_years = df.groupby('year')['rating'].mean().sort_index()

st.bar_chart(rating_years, horizontal=True)



#Question 4:

st.caption("4. What are the 5 best-rated movies that have at least 50 ratings? At least 150 ratings?")
movie_stats = df.groupby('title').agg(
    mean_rating=('rating', 'mean'),
    num_ratings=('rating', 'count')
)

over_50 = movie_stats[movie_stats['num_ratings'] >= 50]

top5_over_50 = over_50.sort_values('mean_rating', ascending=False).head(5)

st.write("Top 5 movies with at least 50 ratings:")
st.dataframe(top5_over_50)  

over_150 = movie_stats[movie_stats['num_ratings'] >= 150]
top5_over_150 = over_150.sort_values('mean_rating', ascending=False).head(5)

st.write("Top 5 movies with at least 150 ratings:")
st.dataframe(top5_over_150)
