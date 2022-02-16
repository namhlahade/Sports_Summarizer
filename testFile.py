import requests
import time
from TextScrape import textDict
from TextScrape import MLBtextDict
import json

for text in textDict.keys():

    url = "https://api.meaningcloud.com/summarization-1.0"

    payload={
        'key': 'a186f0762d84d855c20596808adba62f',
        'txt': textDict[text][1],
        'sentences': '5'
    }

    response = requests.post(url, data=payload)

    #print('Status code:', response.status_code)
    #print(response.json())
    diction = response.json()
    #print(diction['summary'])
    summary = diction['summary']
    newSum = summary.replace('[...]','')
    textDict[text][1] = newSum
    time.sleep(1)