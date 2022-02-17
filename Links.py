NBAurls = []
MLBurls = []
finalImageList = []
MLBImageList = []
NBAImageList = []
NHLImageList = []
NHLurls = []

from bs4 import BeautifulSoup
import requests

NFLURL = "https://www.nfl.com/news/all-news"
 
page = requests.get(NFLURL)
soup = BeautifulSoup(page.content, "html.parser")
images = soup.find_all('img')
imageList = []
 
section = soup.find_all('a')
 
co = 0
unfilteredNFLURLDict = {}
for link in section:
  try:
     fig = link.find('figure')
     pic = fig.find('picture')
     img = pic.find('img')
     image = img.get('src')
     image = image.replace("/t_lazy","")
     unfilteredNFLURLDict['https://www.nfl.com' + link.get('href')] = image
 
  except:
     co = co + 1
 
 
 
NFLurls = list(unfilteredNFLURLDict.keys())

finalImageList = list(unfilteredNFLURLDict.values())

 
 
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
  div2 = aTag.find('div')
  fig = div2.find('figure')
  img = fig.find('img')
  NBAImageList.append(img.get('src'))
#print(NBAurls)


unfilteredMLB = {}
MLBURL = "https://www.cbssports.com/mlb/"
page3 = requests.get(MLBURL)
soup3 = BeautifulSoup(page3.content, "html.parser")
ul = soup3.find('ul',{'tournament-latest-news load-more-content-wrapper'})
divTag = ul.find('div',{'data-component':'loadMore'})
rows = divTag.find_all('ul',{'class':'row article-list-pack-row'})

for row in rows:
   l = row.find_all(['li'])
   for li in l:
      div = li.find('div',{'class','article-list-pack-image'})
      aTag = div.find('a')

      theUrl = 'https://www.cbssports.com' + aTag.get('href')

      fig = aTag.find('figure',{'class':'img'})
      image = fig.find('img')
      src = image.get('data-lazy')
      MLBImageList.append(src)
      MLBurls.append(theUrl)

unfilteredNHL = {}
NHLurl = 'https://www.cbssports.com/nhl/'
page4 = requests.get(NHLurl)
soup4 = BeautifulSoup(page4.content, "html.parser")
ul = soup4.find('ul',{'arena-pack-list-wrapper load-more-content-wrapper'})
divTag = ul.find('div',{'data-component':'loadMore'})
rows = divTag.find_all('ul',{'class':'row article-list-pack-row'})

for row in rows:
   l = row.find_all(['li'])
   for li in l:
      try:
         div = li.find('div',{'class','article-list-pack-image'})
         aTag = div.find('a')
         
         theUrl = 'https://www.cbssports.com' + aTag.get('href')

         fig = aTag.find('figure',{'class':'img'})
         image = fig.find('img')
         src = image.get('data-lazy')
         NHLImageList.append(src)
         NHLurls.append(theUrl)

      except AttributeError:
         x = 5