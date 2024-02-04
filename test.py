import glob
import os

# files = glob.glob("*cycle*.log")
# files.sort(key=os.path.getmtime)
# print("/n".join(files))

# images_path = 'images/'
# images_path = glob.glob(os.path.join(images_path, "*.*")) 
# # images_path.sort(key = os.path.getmtime)
# for i in images_path:
#     print(i)

# cwd = os.getcwd()
# img_name = "Aamir-Khan.jpg"
# read_image_path = os.path.join(cwd, 'static', 'img', img_name)

# print(read_image_path)

# print(os.getcwd())

# name = 'Anant Pawar'
# # name = name.title()
# name1 = name.split()
# # name = '_'.join(name)
# print(name)
# print(name1)

# try:
#     from googlesearch import search
# except ImportError:
#     print("No module named 'google' found")
 
# to search
# query = "katrina kaif twitter screen name"
# from googleapi import google
# num_page = 3
# search_results = google.search(query, num_page)
# res = search(query, tld="co.in", num=5, stop=5, pause=2)

# link = ''

# for j in res:
#     if str(j).find('twitter') != -1:
#         link = j
#     # print(j)
#         break
# lst = link.split('/')
# screen_name = lst[len(lst)-1]
# pos = screen_name.find('?')
# if pos != -1:
#     screen_name = screen_name[:pos]
# print(screen_name)
# print(lst)
# for j in res:
#     print(j)
#     # link = j
    # print(link)
    # break

# s = 'akofficialteam?lang=en'
# pos = s.find('?')
# # s = s[:pos]
# print(pos)


# import cv2
# # import face_recognition

# img_path = 'C:/Users/anant/OneDrive/Desktop/data/Project/MultiFaceRecoginition/images/narendra modi politician.jpg'
# img = cv2.imread(img_path)
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Get the filename only from the initial file path.
# basename = os.path.basename(img_path)
# (filename, ext) = os.path.splitext(basename)
# print(filename)
# Get encoding
# face_encoding returns the 128 measurement of face
# img_encoding = face_recognition.face_encodings(rgb_img)[0]
# print(img_encoding)

# res = face_recognition.compare_faces([img_encoding], img_encoding, 0.6)
# print(res)

# name = "aamir khan actor"
# #  ['aamir', 'khan', 'actor']

# lst_file_name_split = name.split()

# # print(lst_file_name_split)
# lst_idx = len(lst_file_name_split)-1
# lst_file_name_split = lst_file_name_split[0:lst_idx]
# print(lst_file_name_split)
# s = '*'.join(lst_file_name_split)
# print(s)
# self.known_face_names.append()
# from datetime import datetime
# date_str = 'Tue Jan 30 05:46:23 +0000 2024'
# dt = datetime.strptime(date_str, '%a %b %d %H:%M:%S %z %Y')

# date = dt.strftime("%A, %d %b %Y")
# time = dt.strftime("%I:%M %p")
# print(f"{date}--{time}")

# def extract_number(s):
#     res = ''
#     for i in s:
#         if i.isalpha():
#             res += str(i)
#     print(res)

# extract_number('singer234')
# from pyshorturl import TinyUrlcom
# service = TinyUrlcom()
# short_url = service.shorten_url('https://www.google.co.in/')
# print (short_url)
# s = 'my name is   good   '
# res = s.split()
# print(res, len(res))
# from googlesearch import search
# name = 'animal movie 2023 image'

# res = search(name, tld="co.in", num=5, stop=5, pause=2)
# url = str(next(res))
# face_name = ' '.join((url.split('/')[-1]).split('_'))
# print(face_name)
# # link = ''
# for j in res:
#     print(j)
#     # if str(j).find('twitter') != -1:
    #     link = j
    # # print(j)
    #     break
# lst = link.split('/')
# screen_name = lst[len(lst)-1]
# pos = screen_name.find('?')
# if pos != -1:
#     screen_name = screen_name[:pos]
# print(screen_name)
import sys
print(sys.version)
import os
cwd = os.getcwd()
# pathi = os.path.join(cwd, 'static', 'img', 'img1.jpeg')
# os.unlink(pathi)
# def delete_files_in_folder(folder_path):
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#         print(os.path.basename(file_path))
#         # try:
#         #     if os.path.isfile(file_path):
#         #         os.unlink(file_path)
#         # except Exception as e:
#         #     print(f"Failed to delete {file_path}. Reason: {e}")

# # Usage example
# cwd = os.getcwd()
# folder_path = os.path.join(cwd, 'images')
# delete_files_in_folder(folder_path)

import requests
from bs4 import BeautifulSoup

def get_images():
    name_actor = 'salman khan'
    name_actor = name_actor.lower() + ' movies list'
    gs = requests.get('https://www.google.co.in/search?tbm=isch&q=kick movie full hd image')
    soup = BeautifulSoup(gs.text, 'html.parser')
    # print(soup)
    img_url = ''
    img_tags = soup.findAll('img')[1:2]
    print(img_tags[0]['src'])
    # print(img_tags)
    # for img in img_tags:
    #     if 'https' in str(img):
    #         img_url = str(img)
    # return img_url
# get_images()
# import requests
# from bs4 import BeautifulSoup

# def get_movie_posters(actor_name):
#     # Search for the actor's movies on Google Images
#     url = f"https://www.google.com/search?tbm=isch&q={actor_name}+movies"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract image URLs
#     image_urls = []
#     for img in soup.find_all('img'):
#         image_urls.append(img['src'])

#     return image_urls

# # Example usage
# actor_name = "Salman Khan"
# movie_posters = get_movie_posters(actor_name)

# # Print movie poster URLs
# for poster_url in movie_posters:
#     print(f"Poster URL: {poster_url}")
# import requests
# from bs4 import BeautifulSoup

# def get_movie_posters(actor_name):
#     # Search for the actor's movies on Google Images
#     url = f"https://www.google.com/search?tbm=isch&q={actor_name}+movies"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract movie information and image URLs
#     movie_info = []
#     for div in soup.find_all('div', class_='t0fcAb'):
#         img = div.find('img')
#         if img:
#             poster_url = img['src']
#             title_and_year = div.find('div', class_='sD6uYe').text
#             title, year = title_and_year.split(' - ')
#             movie_info.append((title.strip(), year.strip(), poster_url))

#     return movie_info

# # Example usage
# actor_name = "Salman Khan"
# movie_info = get_movie_posters(actor_name)

# # Print movie titles, years, and poster URLs
# for title, year, poster_url in movie_info:
#     print(f"Title: {title} ({year})")
#     print(f"Poster URL: {poster_url}")
#     print()

