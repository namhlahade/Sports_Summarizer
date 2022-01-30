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
    #print(url)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        divTag = soup.find('div', {'class': 'nfl-c-article__container'})
        textDivs = divTag.find_all('div', {'class': 'nfl-c-body-part nfl-c-body-part--text'})
        title = soup.find('h1', {'class':'nfl-c-article__title'}).get_text()
        info = ""
        for paragraph in textDivs:
            pTag = paragraph.find('p')
            info = info + pTag.get_text()
        textDict[url] = [title, info]
    except AttributeError:
        print('URL is not good!')