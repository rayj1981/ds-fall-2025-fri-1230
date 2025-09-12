import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('/workspaces/ds-fall-2025-fri-1230/Week-03-EDA-and-Dashboards/data/movie_ratings.csv')

#cleans the data drop for null values
df = df.dropna()
#drops all duclipates


genre_counts = df['genres'].value_counts()
print(genre_counts)

st.bar_chart(genre_counts)