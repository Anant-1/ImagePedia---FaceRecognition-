import requests
from bs4 import BeautifulSoup

def get_wiki_data(name):
    if name == 'Ms_Dhoni':
        name = 'MS_Dhoni'
    url = 'https://en.wikipedia.org/wiki/' + name
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    paras = soup.find_all('p')
    wiki_text = ''
    cnt = 0
    for i in range(len(paras)):
        if len(paras[i].text) >= 200:
            print(len(paras[i].text))
            wiki_text += paras[i].text+'\n'
            cnt += 1
        if cnt == 5:
            break
    return wiki_text, url

l, u = get_wiki_data('Narendra_Modi')
print(l, u)