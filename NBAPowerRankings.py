nbapowerrankings = []
from http import cookies
from urllib import request
from matplotlib.pyplot import text
import requests
from pandas import *
from bs4 import BeautifulSoup

NBAurl = "https://www.cbssports.com/nba/powerrankings/"

page = requests.get(NBAurl)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find('table',{'class':'table-power-rankings'})
body = table.find('tbody')

rankingRows = body.find_all('tr',{'class':'team-rankings-stats'})

teamRank = 1
for rank in rankingRows:
    td = rank.find('td',{'class':'cell-left team'})
    a = td.find('a')
    teamName = a.find('span',{'class','team-name'}).get_text().strip()

    record = rank.find('td',{'class':'cell-right'}).get_text().strip()
    
    nbapowerrankings.append({'Name':teamName, 'Record':record, 'Rank':teamRank})

    teamRank = teamRank + 1

