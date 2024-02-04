from flask import Flask, render_template, request, redirect
import os, glob, requests, cv2
from algorithm.main import *
import utils.fetch_wiki as fetch_wiki, utils.fetch_yt_data as fetch_yt_data, utils.fetch_movie_data as fetch_movie_data, utils.fetch_twitter as fetch_twitter
import utils.get_google_image as ggi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def load_home_page():
    try: 
        cwd = os.getcwd()
        default_value = '0'
        name = request.form.get('name', default_value)
        profession = request.form.get('profession', default_value)
        
        if name is not None and  name != '0' and profession is not None and profession != '0':
            print('name aa gya : ', name)
            read_image_path = os.path.join(cwd, 'static', 'img', 'img1.jpeg')
            person_image = cv2.imread(read_image_path)
            img_name = name + ' ' + profession + ' 1' + ".jpeg"
            save_path = os.path.join(cwd, 'images', img_name)
            cv2.imwrite(save_path, person_image)

            images_from_google = ggi.get_images(name)
            i = 2
            for image in images_from_google:
                response = requests.get(image)
                if response.status_code == 200:
                    # Save the image to the specified path
                    img_name = name + ' ' + profession + ' ' + str(i) + ".jpeg" 
                    save_path = os.path.join(cwd, 'images', img_name)
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print("Image saved successfully.")
                else:
                    print("Failed to download the image.")
                    raise Exception('Could not save image')
                i+=1
            folder_path = os.path.join(cwd, 'images')
            images_path = glob.glob(os.path.join(folder_path, "*.*"))
            sfr = SimpleFacerec()
            sfr.load_old_data_from_file()
            # If we successfully fetched encodings then we delete the images
            if sfr.write_data_file(images_path):
                sfr.delete_files_in_folder(folder_path)
    except Exception as e:
        print('Error occured ', e)    
    return render_template('index.html')

@app.route('/about')
def load_about_page():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search_image():
    try:
        if request.method == 'POST':
            #Getting image and sending to searchpage.html
            global  img_name
            img_name = 'img1.jpeg'
            cwd = os.getcwd()
            save_path = os.path.join(cwd, 'static', 'img', img_name)

            img_link = request.form.get('searchInputByLink', '-1')
            if img_link != None and img_link != '-1' and img_link != '':
                print('img_link: ', img_link)
                response = requests.get(img_link)
                if response.status_code == 200:
                    # Save the image to the specified path
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print("Image saved successfully.")
                else:
                    print("Failed to download the image.")
                    raise Exception('Could not save image')
            else:
                print('in else')
                img_file = request.files['searchinputByUploading']
                img_file.save(dst=save_path)

            #Getting image name and image profession and sending to searchpage.html
            #calling main_fun of main.py
            global face_name, face_profession
            face_name, face_profession = main_fun(img_name)
            face_name = face_name[0].title()
            face_profession = face_profession[0].capitalize()
            if face_name == 'Unknown' and face_profession == 'Unknown':
                raise Exception('No image found')
            #Getting wiki data and sending to the searchpage.html
            global wiki_text, wiki_url
            wiki_text, wiki_url = fetch_wiki.get_wiki_data(face_name)
            face_name = ' '.join((wiki_url.split('/')[-1]).split('_'))
        return render_template('searchpage.html', img_name = img_name, face_name = str(face_name), face_profession = str(face_profession), wiki_text = wiki_text, wiki_url = wiki_url)
            
    except Exception as e:
        print("Error in Searching image ", e)
        return redirect('notFound')

@app.route('/notFound', methods=['GET', 'POST'])
def notfound():
    return render_template('notFound.html')

@app.route('/youtube', methods=['GET', 'POST'])
def get_songs():
    all_yt_songs = []
    # if face_profession == 'Actor' or face_profession == 'Actress' or face_profession == 'Singer':
    all_yt_songs = fetch_yt_data.get_yt_data(face_name, face_profession)
    # print(all_yt_songs)
    return render_template('youtubelist.html', all_yt_songs=all_yt_songs, face_name = face_name, face_profession = face_profession)

@app.route('/movies', methods=['GET', 'POST'])
def get_movies():
    if face_profession == 'Actor' or face_profession == 'Actress':
        all_movie_list = fetch_movie_data.get_movies_data(face_name)
    return render_template('movielist.html', all_movie_list=all_movie_list, face_name=face_name)

@app.route('/tweets', methods=['GET', 'POST'])
def get_tweets():
    all_tweets, avatar, description = fetch_twitter.get_tweets(face_name)
    return render_template('tweetlist.html', all_tweets=all_tweets, face_name=face_name, description=description, avatar=avatar) 
if __name__ == '__main__':
    app.run(debug = True)