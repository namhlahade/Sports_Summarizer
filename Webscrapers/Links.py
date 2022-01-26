NBAurls = []
NFLurls = []
MLBurls = []
from bs4 import BeautifulSoup
import requests

NFLURL = "https://www.nfl.com/news/all-news"

page = requests.get(NFLURL)
soup = BeautifulSoup(page.content, "html.parser")

section = soup.find_all('a')
for divider in section:
    if '/news' in divider.get('href'):
        if 'https:' not in divider.get('href'):
           NFLurls.append('https://www.nfl.com' + divider.get('href'))

#print(NFLurls)
#print('\n')
NBAURL = 'https://www.nba.com/news/category/top-stories'
 
page2 = requests.get(NBAURL)
soup2 = BeautifulSoup(page2.content, "html.parser")

divTag = soup2.find('div', {'class': 'lg:pr-3 lg:w-3/4'})
 
uList = divTag.find('ul')
list = uList.find_all('li')
 
for li in list:
   div = li.find('div')
   article = div.find('article')
   aTag = article.find('a')
   NBAurls.append('https://www.nba.com' + aTag.get('href'))
 
#print(NBAurls)

MLBURL = "https://www.yardbarker.com/mlb"
page3 = requests.get(MLBURL)
soup3 = BeautifulSoup(page3.content, "html.parser")
for link in soup3.find_all('a', href=True):
   if ('/mlb/articles/' in link['href']):
      if ('https://www.yardbarker.com' + link['href'] not in MLBurls):
         MLBurls.append('https://www.yardbarker.com' + link['href'])
