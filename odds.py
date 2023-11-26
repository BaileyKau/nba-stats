from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import requests

marketList = ['player_assists_over_under', 'player_assists_points_over_under', 
'player_assists_points_rebounds_over_under', 'player_assists_rebounds_over_under', 
'player_blocks_over_under', 'player_blocks_steals_over_under', 'player_points_over_under',
'player_points_rebounds_over_under', 'player_rebounds_over_under', 'player_steals_over_under',
'player_threes_over_under', 'player_turnovers_over_under']

statList = [['AST'], ['AST', 'PTS'], ['AST','PTS','REB'], ['AST','REB'], ['BLK'], ['BLK','STL'], ['PTS'], ['PTS', 'REB'], 
['REB'], ['STL'], ['FG3M'], ['TOV']]

strList = ['assists', 'assists and points', 'assists, points and rebounds', 'assists and rebounds', 'blocks', 'blocks and steals', 'points', 'points and rebounds', 'rebounds', 'steals', '3s made', 'turnovers']

propList = {}

# Loop through the possible markets
for x in range(len(marketList)):
    props = requests.get(f'https://api.prop-odds.com/v1/fantasy_snapshot/nba/{marketList[x]}?api_key=qGf11XMSPQ3RYQH5FHKbOc9A2K9HwZADvCUeiaFLJ8').json()
    if len(props) == 1:
        print("Props have ended! Try again tomorrow.")
        exit(1)
    else:
        props = props['fantasy_books'][0]['market']['lines']
        for y in range(len(props)):
            playerName = str(props[y]['participant_name'])
            line = str(props[y]['line'])

            player = players.find_players_by_full_name(playerName)
            ovrCounter = 0
            if player:
                this_season = playergamelog.PlayerGameLog(player_id=player[0]['id'], season='2023-24', season_type_all_star='Regular Season').get_data_frames()[0]
                for z in range(len(this_season)):
                    lineCheck = 0
                    for stat in statList[x]:
                        lineCheck += this_season[stat].iloc[z]
                    if (float(lineCheck) > float(line)):
                        ovrCounter = ovrCounter + 1
                propList[playerName + " " + line + " " + strList[x]] = ovrCounter/len(this_season)
for prop in propList:
    print(prop + ": " + propList[prop])

        

