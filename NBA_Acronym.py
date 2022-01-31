from http import cookies
from urllib import request
from matplotlib.pyplot import text
import requests
import pandas as pd
nbaAcronyms = {}
df = pd.read_csv("/Users/namhlahade/Documents/GitHub/Sports_Summarizer/NBA_AcronymFile.txt")
listObject = df['Acronym - Name'].tolist()

for team in listObject:
    x = team.split("\t- ")
    if len(x) != 1:
        teamName = x[1].split()
        name = teamName[-1]
        if name == 'Blazers':
            name = 'Trail Blazers'
        nbaAcronyms[name] = x[0]

nbaAcronyms['Rockets'] = 'HOU'
nbaAcronyms['Clippers'] = 'LAC'
nbaAcronyms['Spurs'] = 'SA'