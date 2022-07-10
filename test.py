import glob
import os

# files = glob.glob("*cycle*.log")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

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


from PIL import Image
import requests
from io import BytesIO
url = 'https://akm-img-a-in.tosshub.com/indiatoday/images/story/202205/Untitled_design_-_2022-05-12T2.png?TZreWdL_ak6ZBGfzn3hUiAudI_SBaqKR&size=770:433'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

