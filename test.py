import glob
import os

# files = glob.glob("*cycle*.log")
# files.sort(key=os.path.getmtime)
# print("/n".join(files))

# images_path = 'images/'
# images_path = glob.glob(os.path.join(images_path, "*.*")) 
# images_path.sort(key = os.path.getmtime)
# print(images_path)

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
query = "katrina kaif twitter screen name"
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


import cv2
import face_recognition

img_path = 'C:/Users/anant/OneDrive/Desktop/data/Project/MultiFaceRecoginition/images/narendra modi politician.jpg'
img = cv2.imread(img_path)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get the filename only from the initial file path.
basename = os.path.basename(img_path)
(filename, ext) = os.path.splitext(basename)
# Get encoding
# face_encoding returns the 128 measurement of face
img_encoding = face_recognition.face_encodings(rgb_img)[0]
print(img_encoding)

res = face_recognition.compare_faces([img_encoding], img_encoding, 0.6)
print(res)