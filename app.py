import streamlit as st
import pandas as pd
from ml_model import get_movie_recommendations

st.title('AI Movies Recommendation System - AbacusAI + Streamlit by Afiz')

movies_data = pd.read_csv('relatedmovies/movies_metadata.csv')
st.subheader(f'Movies List')
st.dataframe(movies_data)

name =  st.text_input("Enter Movie ID to find similar movies", key="name") 

if name:
    movie_name = movies_data[movies_data.movie_id==int(name)].movie.item()
    st.subheader(f'Similar Movies of -> {movie_name}')
    data = get_movie_recommendations('1', name)
    data = [int(value['movie_id']) for value in data]
    st.dataframe(movies_data[movies_data.movie_id.isin(data)])