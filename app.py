import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=68bb59a1b8b658212b109394340c9a4c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/"+ poster_path
    
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:16]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster
        

st.header("Movie Recommendation System")
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or Select movie name ',
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5  = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
        
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])
    
    with col6:
        st.text(recommended_movies_name[5])
        st.image(recommended_movies_poster[5])
    
    with col7:
        st.text(recommended_movies_name[6])
        st.image(recommended_movies_poster[6])
    
    with col8:
        st.text(recommended_movies_name[7])
        st.image(recommended_movies_poster[7])
        
    with col9:
        st.text(recommended_movies_name[8])
        st.image(recommended_movies_poster[8])
    
    with col10:
        st.text(recommended_movies_name[9])
        st.image(recommended_movies_poster[9])
    
    with col11:
        st.text(recommended_movies_name[10])
        st.image(recommended_movies_poster[10])
    
    with col12:
        st.text(recommended_movies_name[11])
        st.image(recommended_movies_poster[11])
    
    with col13:
        st.text(recommended_movies_name[12])
        st.image(recommended_movies_poster[12])
        
    with col14:
        st.text(recommended_movies_name[13])
        st.image(recommended_movies_poster[13])
    
    with col15:
        st.text(recommended_movies_name[14])
        st.image(recommended_movies_poster[14])




