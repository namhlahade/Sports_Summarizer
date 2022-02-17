import requests
import time
from TextScrape import textDict
from TextScrape import MLBtextDict
from TextScrape import NBAtextDict
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

for text2 in MLBtextDict.keys():
    try:
        url = "https://api.meaningcloud.com/summarization-1.0"

        payload={
            'key': 'a186f0762d84d855c20596808adba62f',
            'txt': MLBtextDict[text2][1],
            'sentences': '5'
        }

        response = requests.post(url, data=payload)

        #print('Status code:', response.status_code)
        #print(response.json())
        diction = response.json()
        #print(diction['summary'])
        summary = diction['summary']
        newSum = summary.replace('[...]','')
        MLBtextDict[text2][1] = newSum
        time.sleep(1)
    
    except KeyError:
        print('hello')


for text3 in NBAtextDict.keys():
    try:
        url = "https://api.meaningcloud.com/summarization-1.0"

        payload={
            'key': 'a186f0762d84d855c20596808adba62f',
            'txt': MLBtextDict[text3][1],
            'sentences': '5'
        }

        response = requests.post(url, data=payload)

        #print('Status code:', response.status_code)
        #print(response.json())
        diction = response.json()
        #print(diction['summary'])
        summary = diction['summary']
        newSum = summary.replace('[...]','')
        NBAtextDict[text3][1] = newSum
        time.sleep(1)
    
    except KeyError:
        print('hello')

print(NBAtextDict)