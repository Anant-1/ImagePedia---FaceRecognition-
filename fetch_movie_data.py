import requests
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, movie_name, release_year):
        self.movie_name = str(movie_name)
        self.release_year = str(release_year)
    def __repr__(self):
        return f'{self.movie_name} -- {self.release_year}'


def get_movies_data(name_actor):
    name_actor = name_actor.lower() + ' movies list'
    gs = requests.get('https://www.google.co.in/search?q='+name_actor)
    # https://www.google.com/search?q=shahid kapoor movies list
    # markup = '<div class="RWuggc kCrYT"><div><div class="BNeawe s3v9rd AP7Wnd">Jersey</div></div><div><a> HI </a> <div class="BNeawe tAd8D AP7Wnd">2022</div></div></div>'

    soup = BeautifulSoup(gs.text, 'html.parser')
    # print(soup.prettify())
    # sr = soup.select('div.RWuggc.kCrYT div div')
    movie_names = soup.select('div.RWuggc.kCrYT div div.s3v9rd')
    movie_years = soup.select('div.RWuggc.kCrYT div div.tAd8D')

    all_movie_list = []

    for name, year in zip(movie_names, movie_years):
        name = name.text
        year = year.text
        if name != '' and year.isnumeric():
            mv = Movie(name, year)
            all_movie_list.append(mv)
            # print(name, '->', year)
            # mns.append(name)
            # mys.append(year)
    return all_movie_list
# print(mns)
# print(mys)
# for i in sr:
#     print(i)
# # <div class="RWuggc kCrYT">
#   <div>
#       <a> HI </a>
#       <div class="BNeawe s3v9rd AP7Wnd">Jersey</div>
#   </div>
#   <div>
#       <div class="BNeawe tAd8D AP7Wnd">2022</div>
#   </div>
# </div>

