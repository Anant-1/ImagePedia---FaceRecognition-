import requests
from bs4 import BeautifulSoup

def get_wiki_data(name):
    url = 'https://en.wikipedia.org/wiki/' + name
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    paras = soup.find_all('p')
    wiki_text = ''
    for i in range(len(paras)):
        if len(paras[i].text) >= 10:
            wiki_text += paras[i].text+'\n'
        if i==5:
            break
    
    return wiki_text, url

# l, u = get_wiki_data('Jubin_Nautiyal')
# print(l, u)