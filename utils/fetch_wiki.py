import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_wiki_data(name):
    query = name + " wikipedia in english"
    res = search(query, tld="co.in", num=1, stop=1, pause=2)
    url = str(next(res))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    paras = soup.find_all('p')
    wiki_text = ''
    cnt = 0
    for i in range(len(paras)):
        if len(paras[i].text) >= 200:
            # print(len(paras[i].text))
            wiki_text += paras[i].text+'\n'
            cnt += 1
        if cnt == 5:
            break
    return wiki_text, url

# l, u = get_wiki_data('vikkky kauushal')
# print(l, u)