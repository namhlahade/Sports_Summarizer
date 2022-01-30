mlbAbbreviations = {}
mlbPowerRankings = []
from http import cookies
from urllib import request
from matplotlib.pyplot import text
import requests
from pandas import *
from bs4 import BeautifulSoup

MLBurl = "https://www.cbssports.com/mlb/powerrankings/"

page = requests.get(MLBurl)
soup = BeautifulSoup(page.content, "html.parser")

rankings = soup.find_all('tr',{'class':'team-rankings-stats'})
counter = 1
for rank in rankings:
    tdTag = rank.find('td',{'class':'cell-left team'})
    aTag = tdTag.find('a').get('href')
    newaTag = aTag.replace("https://www.cbssports.com/mlb/teams/","")
    acrnym = newaTag.split("/", 1)
    newaTag2 = aTag.replace("https://www.cbssports.com/mlb/teams/"+acrnym[0] + "/", "")
    teamName = newaTag2.split("/", 1)
    finalTeamName = teamName[0].replace("-"," ").title()
    mlbAbbreviations[finalTeamName] = acrnym[0]
    recordTag = rank.find('td',{'class':'cell-right'}).get_text()
    record = recordTag.strip()

    mlbPowerRankings.append({'Name':finalTeamName, 'Record':record, 'Rank':counter})
    counter = counter + 1