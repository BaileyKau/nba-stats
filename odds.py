from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import requests
import time

marketList = ['player_assists_over_under', 'player_assists_points_over_under', 
'player_assists_points_rebounds_over_under', 'player_assists_rebounds_over_under', 
'player_blocks_over_under', 'player_blocks_steals_over_under', 'player_points_over_under',
'player_points_rebounds_over_under', 'player_rebounds_over_under', 'player_steals_over_under',
'player_threes_over_under', 'player_turnovers_over_under']

statList = [['AST'], ['AST', 'PTS'], ['AST','PTS','REB'], ['AST','REB'], ['BLK'], ['BLK','STL'], ['PTS'], ['PTS', 'REB'], 
['REB'], ['STL'], ['FG3M'], ['TOV']]

strList = ['assists', 'assists and points', 'assists, points and rebounds', 'assists and rebounds', 'blocks', 'blocks and steals', 'points', 'points and rebounds', 'rebounds', 'steals', '3s made', 'turnovers']

propList = {}

for x in range(len(marketList)):
    props = requests.get(f'https://api.prop-odds.com/v1/fantasy_snapshot/nba/{marketList[x]}?api_key=hlgvUjJ9eDQCml6F4H5czQkJig1X0wKJdpNZmVSc').json()
    try:
        props = props['fantasy_books'][0]['market']['lines']
    except:
        print("Props have ended or you have run out of PrizePicks API requests. Try again tomorrow.")
        continue
    for y in range(len(props)):
        playerName = str(props[y]['participant_name'])
        line = str(props[y]['line'])

        player = players.find_players_by_full_name(playerName)
        ovrCounter = 0
        if player:
            playerID = player[0]['id']
            time.sleep(0.6)
            this_season = playergamelog.PlayerGameLog(player_id=playerID, season='2023-24', season_type_all_star='Regular Season').get_data_frames()[0]
            for z in range(len(this_season)):
                lineCheck = 0
                for stat in statList[x]:
                    lineCheck += this_season[stat].iloc[z]
                if (float(lineCheck) > float(line)):
                    ovrCounter = ovrCounter + 1
            propList[playerName + " " + line + " " + strList[x]] = ovrCounter/len(this_season)
propList = dict(sorted(propList.items(), key=lambda item: item[1]))
print("------------------------------------------------------------------------------------------------")
print("Prizepicks: ")
for prop in propList:
    print(str(prop) + ": " + str(propList[prop]))

propList = {}

for x in range(len(marketList)):
    props = requests.get(f'https://api.prop-odds.com/v1/fantasy_snapshot/nba/{marketList[x]}?api_key=Qi9nmikSgDApE4Xi7H6IMZ4AK3iLwGvDcl9BzRjAY').json()
    try:
        props = props['fantasy_books'][1]['market']['lines']
    except:
        print("Props have ended or you have run out of Underdog API requests. Try again tomorrow.")
        continue
    for y in range(len(props)):
        playerName = str(props[y]['participant_name'])
        line = str(props[y]['line'])

        player = players.find_players_by_full_name(playerName)
        ovrCounter = 0
        if player:
            playerID = player[0]['id']
            time.sleep(0.6)
            this_season = playergamelog.PlayerGameLog(player_id=playerID, season='2023-24', season_type_all_star='Regular Season').get_data_frames()[0]
            for z in range(len(this_season)):
                lineCheck = 0
                for stat in statList[x]:
                    lineCheck += this_season[stat].iloc[z]
                if (float(lineCheck) > float(line)):
                    ovrCounter = ovrCounter + 1
            propList[playerName + " " + line + " " + strList[x]] = ovrCounter/len(this_season)
propList = dict(sorted(propList.items(), key=lambda item: item[1]))
print("------------------------------------------------------------------------------------------------")
print("Underdog: ")
for prop in propList:
    print(str(prop) + ": " + str(propList[prop]))

