import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px

# Load the CSV
df = pd.read_csv('/workspaces/ds-fall-2025-fri-1230/Week-03-EDA-and-Dashboards/data/movie_ratings.csv')

# Clean the data
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

genres_by_ratings = df.groupby('genres')['rating']



st.bar_chart(genres_by_ratings, horizontal=True)