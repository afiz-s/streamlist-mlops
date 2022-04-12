import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Recommendation App')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3
st.write('## Users Metadata :sunglasses:')
df = pd.read_csv('./relatedmovies/users_metadata.csv')
st.write(df.head())

# Example 4

st.write('## Movies Metadata :sunglasses:')
df_movies = pd.read_csv('./relatedmovies/movies_metadata.csv')
st.write(df_movies.head())