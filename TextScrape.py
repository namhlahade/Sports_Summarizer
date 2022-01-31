from http import cookies
from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup
from Links import NBAurls
from Links import NFLurls
from Links import MLBurls
from Links import finalImageList

textDict = {}
MLBtextDict = {}
finalNFLimages = []
MLBImageList = []

imageCounter = 1
NFLurlDict = {}
for url in NFLurls:
    NFLurlDict[url] = finalImageList[imageCounter]
    imageCounter = imageCounter + 1


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
        finalNFLimages.append(NFLurlDict[url])
    except AttributeError:
        print('URL is not good!')

flagVariable = False
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
        articleTitle = soup.find('div',{'class':'art_headline'})
        hTag = articleTitle.find('h1').get_text()

        try:
            image = soup.find('div',{'class':'lzy it-medium_16_9'})
            img = image.find('img')
            src = img.get('src')
            MLBImageList.append(src)
            if flagVariable == True:
                MLBtextDict[url] = [hTag, info]
        except AttributeError:
            print('Cannot find Image')

        flagVariable = True
    except AttributeError:
        print('URL is not good!')