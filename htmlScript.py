from PowerRankings import powerRanks
from PowerRankings import NFLImages
from PowerRankings import newUrl
from PowerRankings import abbreviations
from Links import MLBImageList, NHLImageList
from testFile import textDict
from testFile import MLBtextDict
from testFile import NBAtextDict
from testFile import NHLtextDict
from MLBPowerRankings import MLBImages
from MLBPowerRankings import mlbPowerRankings
from MLBPowerRankings import MLBurl
from TextScrape import finalNFLimages
from NBAPowerRankings import NBAurl
from NBAPowerRankings import nbapowerrankings
from NBAPowerRankings import NBAImages
from NHLPowerRankings import NHLUrl, nhlpowerrankings, NHLImages
from NBA_Acronym import nbaAcronyms
from Links import NBAImageList

    # takes list of powerRankings data and converts it into HTML template


htmlStr = """
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<!DOCTYPE html>
<html lang="en" >
<head>
    <link rel="stylesheet" href="tables.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports Brew</title>
    <style>
        body{
            background-color: white;
        }
        .title-headers{
            font-size: 25px;
            font-weight: bold;
            font-family: sans-serif;
        }
        .power-rankings{
            border: 10px solid black;
            border-collapse: collapse;
            background-color: white;
            border-radius: 5px;
            border: 1px solid black;
            text-align: center;
            vertical-align: middle;
            font-family: sans-serif;
            margin: 10px auto;
        }
        .body-table{
            border-collapse: separate;
            background-color: white;
            border-radius: 15px;
            border: 1px solid lightgrey;
            text-align: center;
            font-family: sans-serif;
            margin: 15px auto;
        }
        .title-table{
            border-collapse: separate;
            background-color: white;
            border-radius: 15px;
            border: 1px solid lightgrey;
            /*box-shadow: 0px 10px 30px 5px rgba(0,0,0,.15);*/
            font-size: 100px;
            margin: 15px auto;
            text-align: center;
            font-family: sans-serif;
            
        }
    </style>
</head>
<body>
    <table class = "title-table" width=700>
        <tr>
            <td colspan = "3">Sports Brew</td>
        </tr>
    </table>
    <table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href=\"""" + newUrl + """\">NFL Power Rankings</a></td>
        </tr>
        <tr>
            <td>
                <table class = "power-rankings" colspan = "3" border = "1" width=500>
                    <tr>
                        <td>Team Name</td>
                        <td>Record</td>
                        <td>Rank</td>
                    </tr>

                    <tbody>
                        <tbody id="myTable">"""
counter = 1
for rank in powerRanks:
    if counter <= 10:
        row = "<tr>"
        row = row + "\n<td>" + rank.get('Name') + " <img src=" + NFLImages[counter - 1] + " width=\"50\" height = \"50\">" + "</td>"
        row = row + "\n<td>" + rank.get('Record') + "</td>"
        row = row + "\n<td>" + str(rank.get('Rank')) + "</td>"
        row = row + "\n</tr>"
        htmlStr = htmlStr + row
    counter = counter + 1

htmlStr = htmlStr + '''
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table>'''
countVariable = 0
flagVar = 1
articleTitleInfo = ''
for text in textDict.keys():
    if flagVar <= 3:
        header = textDict[text][0]
        info = textDict[text][1]
        articleTitleInfo = articleTitleInfo + '''<table class = "body-table" width=700>
            <tr>
                <th><a href=\"''' + text + '''\">''' + header + '''</a></th>
            </tr>
            <tr>
            <td>''' + """<a href=\"""" + text + """\">""" + '''<img src=\"''' + finalNFLimages[countVariable] + '''\" alt="Flowers in Chania" width = "700"></a></td>
            </tr>
            <tr>
                <td>''' + info + '''</td>
            </tr>
        </table>
        '''
        countVariable = countVariable + 1
        flagVar = flagVar + 1
htmlStr = htmlStr + articleTitleInfo
htmlStr = htmlStr +  """    <table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href=\"""" + MLBurl + """\">MLB Power Rankings</a></td>
        </tr>
        <tr>
            <td>
            <table class = "power-rankings" colspan = "3" border = "1" width=500>
                    <tr>
                        <td>Team Name</td>
                        <td>Record</td>
                        <td>Rank</td>
                    </tr>

                    <tbody>
                        <tbody id="myTable">"""
counter = 1
for rank in mlbPowerRankings:
    if counter <= 10:
        row = "<tr>"
        row = row + "\n<td>" + rank.get('Name') + " <img src=" + MLBImages[counter - 1] + " width=\"40\" height = \"40\">" + "</td>"
        row = row + "\n<td>" + rank.get('Record') + "</td>"
        row = row + "\n<td>" + str(rank.get('Rank')) + "</td>"
        row = row + "\n</tr>"
        htmlStr = htmlStr + row
    counter = counter + 1

htmlStr = htmlStr + '''
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table>'''



countVariable = 1
flagVar = 1
articleTitleInfo = ''
for text in MLBtextDict.keys():
   if flagVar <= 3:
       header = MLBtextDict[text][0]
       info = MLBtextDict[text][1]
       articleTitleInfo = articleTitleInfo + '''<table class = "body-table" width=700>
           <tr>
               <th><a href=\"''' + text + '''\">''' + header + '''</a></th>
           </tr>
           <tr>
           <td>''' + """<a href=\"""" + text + """\">""" + '''<img src=\"''' + MLBImageList[countVariable] + '''\" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>''' + info + '''</td>
           </tr>
       </table>
       '''
       countVariable = countVariable + 1
       flagVar = flagVar + 1
htmlStr = htmlStr + articleTitleInfo

htmlStr = htmlStr + """<table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href=\"""" + NBAurl + """\">NBA Power Rankings</a></td>
        </tr>
        <tr>
            <td>
                <table class = "power-rankings" colspan = "3" border = "1" width=500>
                    <tr>
                        <td>Team Name</td>
                        <td>Record</td>
                        <td>Rank</td>
                    </tr>

                    <tbody>
                        <tbody id="myTable">"""
counter = 1
for rank in nbapowerrankings:
    if (counter <= 10):
        row = "<tr>"
        row = row + "\n<td>" + rank.get('Name') + " <img src=" + NBAImages[counter - 1] + " width=\"50\" height = \"50\">" + "</td>"
        row = row + "\n<td>" + rank.get('Record') + "</td>"
        row = row + "\n<td>" + str(rank.get('Rank')) + "</td>"
        row = row + "\n</tr>"
        htmlStr = htmlStr + row
    counter = counter + 1

htmlStr = htmlStr + '''
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table>'''



countVariable = 1
flagVar = 1
articleTitleInfo = ''
for text in NBAtextDict.keys():
   if flagVar <= 3:
       header = NBAtextDict[text][0]
       info = NBAtextDict[text][1]
       articleTitleInfo = articleTitleInfo + '''<table class = "body-table" width=700>
           <tr>
               <th><a href=\"''' + text + '''\">''' + header + '''</a></th>
           </tr>
           <tr>
           <td>''' + """<a href=\"""" + text + """\">""" + '''<img src=\"''' + NBAImageList[countVariable] + '''\" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>''' + info + '''</td>
           </tr>
       </table>
       '''
       countVariable = countVariable + 1
       flagVar = flagVar + 1
htmlStr = htmlStr + articleTitleInfo


htmlStr = htmlStr + """<table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href=\"""" + NHLUrl + """\">NHL Power Rankings</a></td>
        </tr>
        <tr>
            <td>
                <table class = "power-rankings" colspan = "3" border = "1" width=500>
                    <tr>
                        <td>Team Name</td>
                        <td>Record</td>
                        <td>Rank</td>
                    </tr>

                    <tbody>
                        <tbody id="myTable">"""
counter = 1
for rank in nhlpowerrankings:
    if (counter <= 10):
        row = "<tr>"
        row = row + "\n<td>" + rank.get('Name') + " <img src=" + NHLImages[counter - 1] + " width=\"50\" height = \"50\">" + "</td>"
        row = row + "\n<td>" + rank.get('Record') + "</td>"
        row = row + "\n<td>" + str(rank.get('Rank')) + "</td>"
        row = row + "\n</tr>"
        htmlStr = htmlStr + row
    counter = counter + 1

htmlStr = htmlStr + '''
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table>'''


countVariable = 1
flagVar = 1
articleTitleInfo = ''
for text in NHLtextDict.keys():
   if flagVar <= 3:
       header = NHLtextDict[text][0]
       info = NHLtextDict[text][1]
       articleTitleInfo = articleTitleInfo + '''<table class = "body-table" width=700>
           <tr>
               <th><a href=\"''' + text + '''\">''' + header + '''</a></th>
           </tr>
           <tr>
           <td>''' + """<a href=\"""" + text + """\">""" + '''<img src=\"''' + NHLImageList[countVariable] + '''\" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>''' + info + '''</td>
           </tr>
       </table>
       '''
       countVariable = countVariable + 1
       flagVar = flagVar + 1
htmlStr = htmlStr + articleTitleInfo


htmlStr = htmlStr + '''</body>
</html>'''

print(htmlStr)