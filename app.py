from turtle import Screen
from flask import Flask, render_template, request
import os
from main import *
import fetch_wiki
import fetch_yt_data
import fetch_movie_data
import fetch_twitter
app = Flask(__name__)

@app.route('/')
def load_home_page():
    return render_template('index.html')

@app.route('/about')
def load_about_page():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search_image():
    if request.method == 'POST':
        #Getting image and sending to searchpage.html
        img = request.files['searchinput']
        global  img_name
        img_name = img.filename
        cwd = os.getcwd()
        save_img = os.path.join(cwd, 'static', 'img', img_name)
        img.save(dst=save_img)

        #Getting image name and image profession and sending to searchpage.html
        #calling main_fun of main.py
        global face_name, face_profession
        face_name, face_profession = main_fun(img_name)
        face_name = face_name[0].title()
    
        face_profession = face_profession[0].capitalize()
        
        #Getting wiki data and sending to the searchpage.html
        face_name_wiki = face_name.split()
        face_name_wiki = '_'.join(face_name_wiki)
        global wiki_text, wiki_url
        wiki_text, wiki_url = fetch_wiki.get_wiki_data(face_name_wiki)
        print(wiki_url)
        
        #Getting youtube dalkta and sending to the searchpage.html
        # all_yt_songs = []
        # if face_profession == 'Actor' or face_profession == 'Actress':
        #     all_yt_songs = fetch_yt_data.get_yt_data(face_name)

    return render_template('searchpage.html', img_name = img_name, face_name = face_name, face_profession = face_profession, wiki_text = wiki_text, wiki_url = wiki_url)

@app.route('/songs', methods=['GET', 'POST'])
def get_songs():
    all_yt_songs = []
    if face_profession == 'Actor' or face_profession == 'Actress' or face_profession == 'Singer':
        all_yt_songs = fetch_yt_data.get_yt_data(face_name)
        print(all_yt_songs)
    return render_template('youtubelist.html', all_yt_songs=all_yt_songs, face_name = face_name)

@app.route('/movies', methods=['GET', 'POST'])
def get_movies():
    if face_profession == 'Actor' or face_profession == 'Actress':
        all_movie_list = fetch_movie_data.get_movies_data(face_name)
    return render_template('movielist.html', all_movie_list=all_movie_list, face_name=face_name)

@app.route('/tweets', methods=['GET', 'POST'])
def get_tweets():
    screen_name = fetch_twitter.get_screen_name(face_name)
    if face_name == 'Darshan Raval':
        screen_name = 'DarshanRavalOfc'
    print(screen_name)
    all_tweets = fetch_twitter.get_tweets(screen_name)

    return render_template('tweetlist.html', all_tweets=all_tweets, face_name=face_name) 

if __name__ == '__main__':
    app.run(debug = True)
