from http import cookies
from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup
from Links import NBAurls
from Links import NFLurls
from Links import MLBurls
from Links import NHLurls
from Links import finalImageList
from NHLPowerRankings import NHLUrl

textDict = {}
MLBtextDict = {}
NBAtextDict = {}
NHLtextDict = {}
finalNFLimages = []

imageCounter = 0
NFLurlDict = {}
for url in NFLurls:
    try:
        NFLurlDict[url] = finalImageList[imageCounter]
        imageCounter = imageCounter + 1
    except IndexError:
        break

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
        print('URL is not good! ' + url)

for url in MLBurls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    try:
        head = soup.find('div',{'class':'Article-head'})
        h1 = head.find('h1')
        title = h1.get_text()
        
        div = soup.find('div',{'class':'Article-bodyContent'})
        pTag = div.find_all('p')
        info = ''
        for p in pTag:
            info = info + p.get_text()
        MLBtextDict[url] = [title, info]
    except AttributeError:
        print('URL is not good ' + url)

for url in NBAurls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        constraint = soup.find('div',{'class':'Article_article__2Ue3h'})

        pTag = constraint.find_all('p')
        info = ''
        for p in pTag:
            info = info + p.get_text()

        info = info.replace("Information from The Associated Press was used in this report.","")

        h1 = soup.find('h1', {'class':'h9'})
        title = h1.get_text()
        NBAtextDict[url] = [title, info]
    except AttributeError:
        print('URL is not good ' + url)

for url in NHLurls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    try:
        head = soup.find('div',{'class':'Article-head'})
        h1 = head.find('h1')
        title = h1.get_text()
        
        div = soup.find('div',{'class':'Article-bodyContent'})
        pTag = div.find_all('p')
        info = ''
        for p in pTag:
            info = info + p.get_text()
        NHLtextDict[url] = [title, info]
    except AttributeError:
        print('URL is not good ' + url)


print(NHLtextDict)