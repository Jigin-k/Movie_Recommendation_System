import streamlit as st
import pickle
import pandas as pd


def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:20]

    Recommended_Movies = []
    for i in movie_list:
        Recommended_Movies.append(movies.iloc[i[0]].title)
    return Recommended_Movies

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    "Whats your Favourite Movie...",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = Recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)