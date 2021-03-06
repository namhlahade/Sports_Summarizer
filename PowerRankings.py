powerRanks = []
abbreviations = {}

from http import cookies
from urllib import request
from matplotlib.pyplot import text
import requests
from pandas import *
from bs4 import BeautifulSoup
 
nflAbrvs = read_csv("nfl_teams.csv")
teamNames = nflAbrvs['Name'].tolist()
teamAbrv = nflAbrvs['Abbreviation'].tolist()


for name in teamNames:
    for abr in teamAbrv:
        abbreviations[name] = abr
        teamAbrv.remove(abr)
        break

abbreviations['Washington Commanders'] = 'WAS'
del abbreviations['Washington Football Team']
del abbreviations['NY Jets']
del abbreviations['NY Giants']
abbreviations['New York Giants'] = 'NYG'
abbreviations['New York Jets'] = 'NYJ'

url = 'https://www.nfl.com/news/series/power-rankings-news'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


section = soup.find('section',{'class':'d3-l-grid--outer d3-l-section-row'})
latestPRank = section.find_all('a')
 
newUrl = 'https://www.nfl.com' + latestPRank[0].get('href')
 
page2 = requests.get(newUrl)
soup2 = BeautifulSoup(page2.content, "html.parser")
 
rankingsTags = soup2.find_all('div', {'class':'nfl-o-ranked-item__title'})
recordsTags = soup2.find_all('div', {'class':'nfl-o-ranked-item__info'})
pic = soup2.find_all('div',{'class':'nfl-o-ranked-item'})

NFLImages = []
for pictureItems in pic:
   pictureDiv = pictureItems.find('div',{'class':'nfl-o-ranked-item__image'})
   pictureFig = pictureDiv.find('figure')
   picturePic = pictureFig.find('picture')
   img = picturePic.find('img')
   print(img)
   src = img.get('data-src')
   src = src.replace("/t_lazy", "")
   NFLImages.append(src)

rankings = []
for rank in rankingsTags:
   aTag = rank.find('a')
   rankings.append(aTag.get_text())
 
records = []
for record in recordsTags:
   newRec = record.find('span').get_text()
   records.append(newRec)
 
ranks = []
rank = 1
for r in rankings:
   ranks.append(rank)
   rank = rank + 1
 
i = 0
for record in records:
   newDict = {'Name':rankings[i], 'Record':records[i], 'Rank':ranks[i]}
   powerRanks.append(newDict)
   i=i+1
