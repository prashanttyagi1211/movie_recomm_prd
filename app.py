import streamlit as st
import pickle
import pandas as pd
import requests


# Fetch poster and details from TMDB API
def fetch_movie_details(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    poster_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return poster_url, data


# Recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    recommended_details = []
    for i in movies_list:
        movie_id = movies['movie_id'][i[0]]
        poster, details = fetch_movie_details(movie_id)
        recommended_movies.append(movies['title'][i[0]])
        recommended_posters.append(poster)
        recommended_details.append(details)
    return recommended_movies, recommended_posters, recommended_details


# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie name', movies['title'].values)

if st.button('Recommend'):
    names, posters, details = recommend(selected_movie_name)

    for i in range(len(names)):
        with st.container():
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(posters[i], use_container_width=True)

            with col2:
                st.subheader(names[i])
                st.write(f"**Overview:** {details[i]['overview']}")
                st.write(f"**Release Date:** {details[i]['release_date']}")
                st.write(f"**Rating:** {details[i]['vote_average']} / 10")
                st.write(f"**Genres:** {', '.join([genre['name'] for genre in details[i]['genres']])}")
                tmdb_url = f"https://www.themoviedb.org/movie/{details[i]['id']}"
                st.markdown(f"[More Details on TMDB]({tmdb_url})", unsafe_allow_html=True)