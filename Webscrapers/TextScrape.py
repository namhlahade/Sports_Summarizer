from http import cookies
from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup
from Links import NBAurls
from Links import NFLurls
from Links import MLBurls

textDict = {}

for url in NFLurls:
    URL = url

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        divTag = soup.find('div', {'class': 'nfl-c-article__container'})
        textDivs = divTag.find_all('div', {'class': 'nfl-c-body-part nfl-c-body-part--text'})

        info = ""
        for paragraph in textDivs:
            pTag = paragraph.find('p')
            info = info + pTag.get_text()
        textDict[url] = info
    except AttributeError:
        print('URL is not good!')

for url in NBAurls:
    URL = url

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        divTag = soup.find('div', {'class': 'Article_article__2Ue3h'})

        pTag = divTag.find_all('p')
        info = ""
        for p in pTag:
            info = info + p.get_text()
        textDict[url] = info
    except AttributeError:
        print('URL is not good')

for url in MLBurls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    div = soup.find('div', {'class':'art_body_article'})
    try:
        info = ""
        pTags = div.find_all('p')
        for p in pTags:
            if not p.find('a'):
                info = info + p.get_text()
        textDict[url] = info
    except AttributeError:
        print('URL is not good')

for hel in textDict.keys():
    print(hel)
    print(textDict[hel])