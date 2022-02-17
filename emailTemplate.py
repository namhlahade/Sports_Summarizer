import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('lahadenamh@gmail.com')
EMAIL_PASSWORD = os.environ.get('dukegoogle2024')

contacts = ['lahadenamh@gmail.com', 's.lahade@gmail.com', 'oum.lahade@gmail.com','h.lahade@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Latest Sports New for the Day!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.set_content('This is a plain text email')

msg.add_alternative("""\
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
            <td colspan = "3" class = "title-headers"><a href="https://www.nfl.com/news/nfl-power-rankings-super-bowl-2021-nfl-season">NFL Power Rankings</a></td>
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
                        <tbody id="myTable"><tr>
<td>Los Angeles Rams <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/LA width="50" height = "50"></td>
<td>16-5</td>
<td>1</td>
</tr><tr>
<td>Kansas City Chiefs <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/KC width="50" height = "50"></td>
<td>14-6</td>
<td>2</td>
</tr><tr>
<td>Buffalo Bills <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/BUF width="50" height = "50"></td>
<td>12-7</td>
<td>3</td>
</tr><tr>
<td>Cincinnati Bengals <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/CIN width="50" height = "50"></td>
<td>13-8</td>
<td>4</td>
</tr><tr>
<td>Green Bay Packers <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/GB width="50" height = "50"></td>
<td>13-5</td>
<td>5</td>
</tr><tr>
<td>San Francisco 49ers <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/SF width="50" height = "50"></td>
<td>12-8</td>
<td>6</td>
</tr><tr>
<td>Dallas Cowboys <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/DAL width="50" height = "50"></td>
<td>12-6</td>
<td>7</td>
</tr><tr>
<td>Tennessee Titans <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/TEN width="50" height = "50"></td>
<td>12-6</td>
<td>8</td>
</tr><tr>
<td>Indianapolis Colts <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/IND width="50" height = "50"></td>
<td>9-8</td>
<td>9</td>
</tr><tr>
<td>New England Patriots <img src=https://static.www.nfl.com/t_thumb_squared/f_auto/league/api/clubs/logos/NE width="50" height = "50"></td>
<td>10-8</td>
<td>10</td>
</tr>
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table><table class = "body-table" width=700>
            <tr>
                <th><a href="https://www.nfl.com/news/saints-to-retain-pete-carmichael-as-offensive-coordinator-under-dennis-allen">
              Saints to retain Pete Carmichael as offensive coordinator under Dennis Allen
            </a></th>
            </tr>
            <tr>
            <td><a href="https://www.nfl.com/news/saints-to-retain-pete-carmichael-as-offensive-coordinator-under-dennis-allen"><img src="https://static.www.nfl.com/image/private/t_editorial_landscape_mobile/f_auto/league/kmzrhggx8ah4nuludxyd.jpg" alt="Flowers in Chania" width = "700"></a></td>
            </tr>
            <tr>
                <td>The Saints' offense will have some continuity in the first season of the post-Sean Payton era.NFL Network Insider Ian Rapoport reported Wednesday that Pete Carmichael will remain on Dennis Allen's staff as the team's offensive coordinator. Rapoport added that the Saints conducted several interviews at OC, but elected for staff continuity.Carmichael has been the Saints' offensive coordinator since New Orleans' Super Bowl-winning 2009 season, but under Payton's watch that unit obviously was heavily influenced by the head coach. The offense now will fully be Carmichael's after he occasionally called plays when Payton was at the helm.The Saints offense finished 28th in yards and 19th in points during a 2021 season that saw New Orleans start four different quarterbacks (Jameis Winston, Taysom Hill, Trevor Siemian and Ian Book).</td>
            </tr>
        </table>
        <table class = "body-table" width=700>
            <tr>
                <th><a href="https://www.nfl.com/news/nfl-qb-index-ranking-all-62-starting-qbs-of-the-2021-nfl-season">
              NFL QB Index: Ranking all 62 starting QBs of the 2021 NFL season
            </a></th>
            </tr>
            <tr>
            <td><a href="https://www.nfl.com/news/nfl-qb-index-ranking-all-62-starting-qbs-of-the-2021-nfl-season"><img src="https://static.www.nfl.com/image/private/t_editorial_landscape_mobile/f_auto/league/xatzxew9yruitbuzjzwo.jpg" alt="Flowers in Chania" width = "700"></a></td>
            </tr>
            <tr>
                <td>This is the final, post-Super Bowl rankings of every quarterback who started a game this season -- based on play from the 2021 regular season and the playoffs. Here are my rankings, Nos. 1-62.</td>
            </tr>
        </table>
        <table class = "body-table" width=700>
            <tr>
                <th><a href="https://www.nfl.com/news/nfl-fantasy-football-podcast-super-bowl-fantasy-wrap-up-the-offseason-begins">
              NFL Fantasy Football Podcast: Super Bowl fantasy wrap-up (the offseason begins)
            </a></th>
            </tr>
            <tr>
            <td><a href="https://www.nfl.com/news/nfl-fantasy-football-podcast-super-bowl-fantasy-wrap-up-the-offseason-begins"><img src="https://static.www.nfl.com/image/private/t_editorial_landscape_mobile/f_auto/league/zklixwwajfw7kodof0pq.jpg" alt="Flowers in Chania" width = "700"></a></td>
            </tr>
            <tr>
                <td>Marcas Grant and Michael F. Florio are back for a special new edition of the NFL Fantasy Football Podcast with the offseason officially upon us. To start, Marcas and Michael recap their top fantasy takeaways from Super Bowl LVI, looking ahead to next season's outlook for Cooper Kupp, Ja'Marr Chase and Tee Higgins, Joe Burrow, and Odell Beckham Jr. Then, we hear from Patriots fullback Jakob Johnson, originally from Germany, about the NFL's upcoming expansion into his home country. After that, the experts cover some of the biggest questions answered during the 2021 NFL Playoffs: which players helped or hurt their fantasy draft value the most; and how much stock we should put into playoff performances? Finally, we wrap up the show with our Jerry Jeudy interview conducted last week at Super Bowl LVI Radio Row. The NFL Fantasy Football Podcast is part of the NFL Podcast Network.Apple PodcastsSpotifyNFL.comGoogle Podcasts</td>
            </tr>
        </table>
            <table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href="https://www.cbssports.com/mlb/powerrankings/">MLB Power Rankings</a></td>
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
                        <tbody id="myTable"><tr>
<td>Atlanta Braves <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/ATL.svg width="40" height = "40"></td>
<td>88-73</td>
<td>1</td>
</tr><tr>
<td>Los Angeles Dodgers <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/LAD.svg width="40" height = "40"></td>
<td>106-56</td>
<td>2</td>
</tr><tr>
<td>San Francisco Giants <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/SF.svg width="40" height = "40"></td>
<td>107-55</td>
<td>3</td>
</tr><tr>
<td>Houston Astros <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/HOU.svg width="40" height = "40"></td>
<td>95-67</td>
<td>4</td>
</tr><tr>
<td>Boston Red Sox <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/BOS.svg width="40" height = "40"></td>
<td>92-70</td>
<td>5</td>
</tr><tr>
<td>Tampa Bay Rays <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/TB.svg width="40" height = "40"></td>
<td>100-62</td>
<td>6</td>
</tr><tr>
<td>Milwaukee Brewers <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/MIL.svg width="40" height = "40"></td>
<td>95-67</td>
<td>7</td>
</tr><tr>
<td>St Louis Cardinals <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/STL.svg width="40" height = "40"></td>
<td>90-72</td>
<td>8</td>
</tr><tr>
<td>New York Yankees <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/NYY.svg width="40" height = "40"></td>
<td>92-70</td>
<td>9</td>
</tr><tr>
<td>Toronto Blue Jays <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/mlb/TOR.svg width="40" height = "40"></td>
<td>91-71</td>
<td>10</td>
</tr>
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table><table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.cbssports.com/mlb/news/matt-harvey-could-face-suspension-for-drug-distribution-following-testimony-in-eric-kay-trial-per-report/">
                        Matt Harvey could face suspension for drug distribution following testimony in Eric Kay trial, per report
        </a></th>
           </tr>
           <tr>
           <td><a href="https://www.cbssports.com/mlb/news/matt-harvey-could-face-suspension-for-drug-distribution-following-testimony-in-eric-kay-trial-per-report/"><img src="https://sportshub.cbsistatic.com/i/r/2022/01/13/a3e49ab8-f6de-405e-a7aa-85507d61ab6d/thumbnail/370x208/5aa814e42ba10ec1c6b3d0e7e396ebf1/mlb-lockout-5.png" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Free-agent pitcher Matt Harvey testified on Tuesday as part of the trial concerning ex-Los Angeles Angels employee Eric Kay's role in the death of former pitcher Tyler Skaggs. Kay is accused of providing the drugs to Skaggs that resulted in his death.  Here's part of what Harvey testified about during his time on the stand:Harvey stated that he would provide Skaggs with Percocet pills, and that painkiller usage was common among players in 2019. He also told the court about how, after being told he wasn't traveling with the Angels on what proved to be that fateful road trip, he asked Kay for an oxycodone pill.  Those players are not expected to be suspended since none of them admitted to distributing the drugs to other players.</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.cbssports.com/mlb/news/mlb-lockout-owners-players-expected-to-meet-thursday-to-discuss-economic-issues-per-report/">
                        MLB lockout: Owners, players expected to meet Thursday to discuss economic issues, per report
        </a></th>
           </tr>
           <tr>
           <td><a href="https://www.cbssports.com/mlb/news/mlb-lockout-owners-players-expected-to-meet-thursday-to-discuss-economic-issues-per-report/"><img src="https://sportshub.cbsistatic.com/i/r/2022/02/16/2f895b92-2abe-44b7-9967-ccedded64760/thumbnail/370x208/51252fba95cc63b660cf4ba1972609dc/freeman.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Wednesday was supposed to be the most exciting day on the baseball calendar. It was to be the first day all 30 teams had their spring training camps open, and there is no better time of year.  Baseball's return after the long winter is a glorious day.Alas and alack, MLB and the MLB Players Association remain engaged in the second longest work stoppage in baseball history.  Some teams are holding prospect mini-camps this week.Mini camp for Phillies prospects is underway pic.twitter.com/cQgBwoxex3The owners could lift the lockout at any time.  The owners have shown no indication they are willing to lift the lockout, however.At 77 days and counting, this is the second longest lockout in baseball history, trailing only the 1994-95 strike (232 days).</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.cbssports.com/mlb/news/mlb-rumors-freddie-freeman-could-listen-to-other-offers-orioles-expected-to-sign-shed-long/">
                        MLB rumors: Freddie Freeman could listen to other offers; Orioles expected to sign Shed Long
        </a></th>
           </tr>
           <tr>
           <td><a href="https://www.cbssports.com/mlb/news/mlb-rumors-freddie-freeman-could-listen-to-other-offers-orioles-expected-to-sign-shed-long/"><img src="https://sportshub.cbsistatic.com/i/r/2022/02/16/779f5377-0001-497a-8d2e-e8e2f3856942/thumbnail/370x208/d66473909363c22205be23e0f672cb8a/gettyimages-13589970601.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Major League Baseball's owner-imposed lockout may have caused the offseason to freeze, but that hasn't stopped the occasional rumor from slipping through concerning what teams intend to do if and when the league and the MLB Players Association ratify a new collective bargaining agreement. When that occurs, don't be surprised if Freeman's name surfaces in conjunction with teams other than the Braves. Longtime Atlanta third baseman Chipper Jones suggested as much during an appearance on the Dukes & Bell radio show on Tuesday: "The Braves have made some offers, didn't make him happy," Jones said. "He's being courted by some of the prettiest girls on the block right now, he's gonna listen to them.  He's also homered 12 times and tallied -0.4 Wins Above Replacement, per Baseball Reference's calculations.</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href="https://www.cbssports.com/nba/powerrankings/">NBA Power Rankings</a></td>
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
                        <tbody id="myTable"><tr>
<td>Suns <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/PHO.svg width="50" height = "50"></td>
<td>48-10</td>
<td>1</td>
</tr><tr>
<td>Grizzlies <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/MEM.svg width="50" height = "50"></td>
<td>41-19</td>
<td>2</td>
</tr><tr>
<td>Warriors <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/GS.svg width="50" height = "50"></td>
<td>42-16</td>
<td>3</td>
</tr><tr>
<td>Bucks <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/MIL.svg width="50" height = "50"></td>
<td>36-23</td>
<td>4</td>
</tr><tr>
<td>Heat <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/MIA.svg width="50" height = "50"></td>
<td>37-21</td>
<td>5</td>
</tr><tr>
<td>Cavaliers <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/CLE.svg width="50" height = "50"></td>
<td>35-23</td>
<td>6</td>
</tr><tr>
<td>Mavericks <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/DAL.svg width="50" height = "50"></td>
<td>34-24</td>
<td>7</td>
</tr><tr>
<td>76ers <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/PHI.svg width="50" height = "50"></td>
<td>34-23</td>
<td>8</td>
</tr><tr>
<td>Raptors <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/TOR.svg width="50" height = "50"></td>
<td>32-25</td>
<td>9</td>
</tr><tr>
<td>Celtics <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nba/BOS.svg width="50" height = "50"></td>
<td>34-26</td>
<td>10</td>
</tr>
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table><table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.nba.com/news/anthony-davis-leaves-game-vs-jazz-with-apparent-ankle-injury">Anthony Davis leaves game vs. Jazz with right ankle injury</a></th>
           </tr>
           <tr>
           <td><a href="https://www.nba.com/news/anthony-davis-leaves-game-vs-jazz-with-apparent-ankle-injury"><img src="https://cdn.nba.com/manage/2022/02/gregg-popovich-coaching.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Anthony Davis goes down late in the 2nd quarter vs. Utah. Anthony Davis’ injury woes continued Wednesday against the Jazz as the Lakers star suffered what appeared to be a significant ankle injury late in the second quarter.Davis left his feet to grab a lob pass when he came down on Jazz center Hassan Whiteside. Replays of the incident showed Davis’ right ankle bending at roughly a 90-degree angle before he was helped off the court.Lakers sideline reporter Mike Trudell said initial x-rays were negative, and that Davis will receive treatment over the All-Star break before being re-evaluated when the team reconvenes for the stretch run.X-rays were negative on Anthony Davis' ankle. He’ll receive treatment over the All-Star break, and be re-evaluated when the team gets back.— Mike Trudell (@LakersReporter) February 17, 2022 Davis, who scored 17 points in 17 minutes before he was injured, had only recently returned after missing 17 games with a sprained knee.Even with Wednesday’s appearance, the eight-time All-Star has missed 57 of the Lakers’ 130 games over the past two seasons. </td>
           </tr>
       </table>
       <table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.nba.com/news/spurs-coach-gregg-popovich-passes-wilkens-for-no-2-on-all-time-coaching-wins-list">Spurs coach Gregg Popovich passes Wilkens for No. 2 on all-time coaching wins list</a></th>
           </tr>
           <tr>
           <td><a href="https://www.nba.com/news/spurs-coach-gregg-popovich-passes-wilkens-for-no-2-on-all-time-coaching-wins-list"><img src="https://cdn.nba.com/manage/2022/01/draymond-pass.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Spurs Gregg Popovich needs just three more victories to pass Don Nelson for the most coaching wins in NBA history.Gregg Popovich left Wednesday’s game in Oklahoma City a winner — something he’s done more often than all but one coach in NBA history.With his 1,333rd career victory, the iconic coach of the San Antonio Spurs broke a tie with Hall of Famer Lenny Wilkens to claim sole possession of the No. 2 spot in all-time NBA coaching wins.Three more, and Popovich will be alone at the top. Don Nelson holds the current coaching wins record with 1,335.Congrats to Coach Gregg Popovich of the @spurs for moving up to 2nd on the all-time TOTAL COACHING WINS list! #NBA75 pic.twitter.com/o6b0adBkdu— NBA (@NBA) February 17, 2022Since taking over as the Spurs head coach in 1997, Popovich has made the Spurs synonymous with competence at their worst and dominance at their best. Behind his guidance and Hall-of-Fame talents like David Robinson and Tim Duncan, the Spurs won five NBA championships between 1999 and 2014. Last week Popovich was named one of the 15 Greatest Coaches in league history, an honor given to mark the NBA’s 75th anniversary season.The three-time NBA coach of the Year is one of just six coaches to have worked more than 2,000 regular season games and 26 seasons or more. His career win percentage of .659 is the best in that group. In addition to his NBA accomplishments, Popovich also owns a gold medal from coaching the 2020 Team USA Olympic team.</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.nba.com/news/draymond-green-back-disc-expected-to-return-after-all-star-break">Draymond Green (back/disc) expected to return after All-Star break</a></th>
           </tr>
           <tr>
           <td><a href="https://www.nba.com/news/draymond-green-back-disc-expected-to-return-after-all-star-break"><img src="https://cdn.nba.com/manage/2022/01/010722-zach-lavine-shoots-vs-wizards-cropped.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Draymond Green, who has missed the last 19 games (20 if including the Jan. 9 game vs. Cleveland in which he played seven seconds) due to a lower back/disc injury, is making good progress in his recovery/rehabilitation and it’s anticipated that he will return to play at some point after the All-Star break. He has recently progressed to doing some light on-court activity and will continue to increase his workload moving forward. The next update will be provided when he returns to practice on a date to be determined.</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
        <tr>
            <td colspan = "3" class = "title-headers"><a href="https://www.cbssports.com/nhl/powerrankings/">NHL Power Rankings</a></td>
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
                        <tbody id="myTable"><tr>
<td>Avalanche <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/COL.svg width="50" height = "50"></td>
<td>34-9-4</td>
<td>1</td>
</tr><tr>
<td>Panthers <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/FLA.svg width="50" height = "50"></td>
<td>33-10-5</td>
<td>2</td>
</tr><tr>
<td>Wild <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/MIN.svg width="50" height = "50"></td>
<td>30-12-3</td>
<td>3</td>
</tr><tr>
<td>Penguins <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/PIT.svg width="50" height = "50"></td>
<td>31-11-8</td>
<td>4</td>
</tr><tr>
<td>Rangers <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/NYR.svg width="50" height = "50"></td>
<td>31-13-4</td>
<td>5</td>
</tr><tr>
<td>Maple Leafs <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/TOR.svg width="50" height = "50"></td>
<td>31-12-3</td>
<td>6</td>
</tr><tr>
<td>Lightning <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/TB.svg width="50" height = "50"></td>
<td>32-11-6</td>
<td>7</td>
</tr><tr>
<td>Hurricanes <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/CAR.svg width="50" height = "50"></td>
<td>32-11-4</td>
<td>8</td>
</tr><tr>
<td>Flames <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/CGY.svg width="50" height = "50"></td>
<td>27-13-6</td>
<td>9</td>
</tr><tr>
<td>Golden Knights <img src=https://sportsfly.cbsistatic.com/fly-0161/bundles/sportsmediacss/images/team-logos/nhl/LV.svg width="50" height = "50"></td>
<td>28-17-3</td>
<td>10</td>
</tr>
                        </tbody>
                    </tbody>
                </table>
                <td>
            </td>
        </tr>
    </table><table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.cbssports.com/nhl/news/penguins-star-sidney-crosby-scores-500th-career-goal-becomes-only-second-active-nhl-player-to-hit-milestone/">
                        Penguins star Sidney Crosby scores 500th career goal, becomes only second active NHL player to hit milestone
        </a></th>
           </tr>
           <tr>
           <td><a href="https://www.cbssports.com/nhl/news/penguins-star-sidney-crosby-scores-500th-career-goal-becomes-only-second-active-nhl-player-to-hit-milestone/"><img src="https://sportshub.cbsistatic.com/i/r/2022/02/09/d5ceb141-1216-4df3-b871-d37cad869a4f/thumbnail/370x208/0a6d5657fb046bbdaf88201589df8105/marchand.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Sidney Crosby shot his way into NHL history Tuesday night in Pittsburgh. He and Washington Capitals star Alex Ovechkin are the only active NHL players with at least 500 goals.  5️⃣0️⃣0️⃣ for 8️⃣7️⃣!Sidney Crosby scores his 500th career @NHL goal on the power-play.  Crosby entered the game with 499 career goals over his 17 NHL seasons and 1,076 games, all of which he spent with the Penguins.  Sidney Crosby joins Mario Lemieux (690) as the only players in Penguins history to score 500 goals with the team.</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.cbssports.com/nhl/news/bruins-brad-marchand-suspended-six-games-for-punching-penguins-goalie-tristan-jarry-in-head/">
                        Bruins' Brad Marchand suspended six games for punching Penguins goalie Tristan Jarry in head
        </a></th>
           </tr>
           <tr>
           <td><a href="https://www.cbssports.com/nhl/news/bruins-brad-marchand-suspended-six-games-for-punching-penguins-goalie-tristan-jarry-in-head/"><img src="https://sportshub.cbsistatic.com/i/r/2022/02/09/304d7a42-e240-4e9c-a7d4-e52c8ea07b7f/thumbnail/370x208/ec1a6463981cb5b401c723c1fe32a9e8/gettyimages-1364302610.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>Boston Bruins winger Brad Marchand found himself in hot water yet again on Tuesday. During a game against the Pittsburgh Penguins, Marchand punched Penguins goaltender Tristan Jarry in the head with his right fist during a scrum in front of the net.On Wednesday, Marchand was suspended six games by the NHL for his encounter with Jarry.  "Marchand has been suspended seven times, and fined five times previously."Marchand was given a match penalty for his actions, but that wasn't the end of the encounter with Jarry. While being restrained by a linesman, Marchand swung his stick at Jarry as he skated by.This isn't good from Marchand in the final minute of the game. Punch + stick swing on Jarry pic.twitter.com/yrq9Ek8o4iIn November, Marchand was suspended three games for slewfooting Vancouver Canucks defenseman Oliver Ekman-Larsson.</td>
           </tr>
       </table>
       <table class = "body-table" width=700>
           <tr>
               <th><a href="https://www.cbssports.com/nhl/news/bruins-tuukka-rask-bostons-all-time-winningest-goaltender-announces-retirement-after-15-seasons/">
                        Bruins' Tuukka Rask, Boston's all-time winningest goaltender, announces retirement after 15 seasons
        </a></th>
           </tr>
           <tr>
           <td><a href="https://www.cbssports.com/nhl/news/bruins-tuukka-rask-bostons-all-time-winningest-goaltender-announces-retirement-after-15-seasons/"><img src="https://sportshub.cbsistatic.com/i/r/2022/02/07/b3430e1f-2617-4f41-97a0-f698a3b325e1/thumbnail/370x208/9561b55dd4ddaba26f2b6ac737267d2c/nhl-power-rankings-feb-7.jpg" alt="Flowers in Chania" width = "700"></a></td>
           </tr>
           <tr>
               <td>After a remarkable 15-year NHL career with the Boston Bruins, Tuukka Rask has reached the end: On Wednesday evening, the longtime Bruins goaltender announced his retirement from hockey after a brief comeback attempt following surgery to repair a torn hip labrum lasted just four games.Rask, the No. 21 overall pick in the 2005 NHL Draft and a member of the Bruins' 2011 Stanley Cup-winning team, cited his physical and playing condition post-surgery in choosing to retire. Rask had appeared in just four games this season after signing a one-year contract with the Bruins in January, going 2-2 with a 4.28 goals against average."When I made the decision to have surgery on my hip last summer, I did so knowing that the road to recovery would be challenging. I also knew it was something I would have to do if I wanted to give myself a chance to play my best hockey again," read a statement by Rask.  Therefore, it is with a heavy heart that I announce my retirement from the game of hockey."A statement from Tuukka Rask.#NHLBruins pic.twitter.com/Lae4E8rLfIOriginally drafted by the Toronto Maple Leafs, Rask was traded to the Bruins before he ever played a regular-season NHL game, and he would become one of the franchise's most-prolific players of the last two decades.  The team honored Rask's wishes, allowing him to return to practice in November and December before signing him to a one-year deal in January.</td>
           </tr>
       </table>
       </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('lahadenamh@gmail.com', 'dukegoogle2024')
    smtp.send_message(msg)