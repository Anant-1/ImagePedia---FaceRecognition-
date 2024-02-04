import requests
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, name, release_year, image_url):
        self.movie_name = str(name)
        self.release_year = str(release_year)
        self.image_url = str(image_url)

    def __repr__(self):
        return f'{self.movie_name} -- {self.release_year} -- {self.image_url}'
    
def get_movie_image(movie_name):
    query = movie_name.lower() + ' movie full hd image'
    gs = requests.get('https://www.google.co.in/search?tbm=isch&q='+query)
    soup = BeautifulSoup(gs.text, 'html.parser')
    img_tags = soup.findAll('img')[1:2]
    return str(img_tags[0]['src'])
    # img_tags = soup.findAll('img')
    # for img in img_tags:
    #     if 'https' in str(img):
    #         return str(img)

def get_movies_data(name_actor):
    name_actor = name_actor.lower() + ' movies list'
    gs = requests.get('https://www.google.co.in/search?q='+name_actor)
    # https://www.google.com/search?q=shahid kapoor movies list
    # markup = '<div class="RWuggc kCrYT"><div><div class="BNeawe s3v9rd AP7Wnd">Jersey</div></div><div><a> HI </a> <div class="BNeawe tAd8D AP7Wnd">2022</div></div></div>'

    soup = BeautifulSoup(gs.text, 'html.parser')

    movie_names = soup.select('div.RWuggc.kCrYT div div.s3v9rd')
    movie_years = soup.select('div.RWuggc.kCrYT div div.tAd8D')
    all_movie_list = []

    for name, year in zip(movie_names, movie_years):
        name = name.text
        year = year.text
        image_url = get_movie_image(name)
        if name != '' and year.isnumeric():
            mv = Movie(name, year, image_url)
            all_movie_list.append(mv)
            # print(name, '->', year)
            # mns.append(name)
            # mys.append(year)
        if len(all_movie_list) == 20: 
            break
    return all_movie_list
# print(get_movies_data('salman khan'))

