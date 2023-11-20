from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd
import math

#-----------------------------------------------Player Career Stats------------------------------------------------------------

playerName = input("Enter the player's full name: ")

player = players.find_players_by_full_name(playerName)

# Loop the user input to get the correct answer
#playerID is None
if len(player) != 0:
    playerID = player[0]['id']
#If no players are found
# REMEMBER TO TRY USING NLP LIBRARIES 
else:
    for player in players.find_players_by_first_name(playerName.split(" ")[0]):
        if player['last_name'] == playerName.split(" ")[1]:
            playerID = player['id']
    try:
        playerID
    except NameError:
        for player in players.find_players_by_last_name(playerName.split(" ")[1]):
            if player['first_name'] == playerName.split(" ")[0]:
                playerID = player['id']

    
# Data Frame [0] is the season by season breakdown of statistics 
# Data Frame [1] is the all time totals
career = playercareerstats.PlayerCareerStats(player_id=playerID) 
allTime = career.get_data_frames()[1].loc[0]
perSeason = career.get_data_frames()[0]
gamesPlayed = allTime.loc['GP']
recentSeason = perSeason.iloc[len(career.get_data_frames()[0])-1]
gamesPlayedThisYear = recentSeason.loc['GP']

print("----------------------------------------------------")

statsNeeded = input("""Abbreviations:\n
'PTS' Points\n           
'REB' Rebounds (OREB/DREB)\n      
'AST' Assists\n       
'STL' Steals\n        
'BLK' Blocks\n
'FGA/FGM' Field Goals Attempted/Field Goals Made\n
'PF' Personal Fouls\n
'TOV' Turnovers
----------------------------------------------------
Use '+' for combined statistics: PTS+REB
Enter the statistic needed: """)

statList = statsNeeded.split("+")
allTimeStat = 0
thisSeasonStat = 0
for stat in statList:
    allTimeStat += allTime[stat]
    thisSeasonStat += recentSeason[stat]

print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("| All time, " + playerName + " has: \n|")
allTimeAvg = round(allTimeStat/gamesPlayed, 2)
print("| " + str(allTimeStat) + " " + statsNeeded + " in " + str(gamesPlayed) + " games to average " + str(allTimeAvg) + " " + statsNeeded)

print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("| This season, " + playerName + " has: \n|")
thisSeasonAvg = round(thisSeasonStat/gamesPlayedThisYear, 2)
print("| " + str(thisSeasonStat) + " " + statsNeeded + " in " + str(gamesPlayedThisYear) + " games to average " + str(thisSeasonAvg) + " " + statsNeeded)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")

line = float(input("| What is the line?\n"))

#-----------------------------------------------Box Score/Individual Games------------------------------------------------------------
season = '2023-24'

# Create the player game log endpoint
player_game_log = playergamelog.PlayerGameLog(player_id=playerID, season=season, season_type_all_star='Regular Season')

# Call the API and get the result
player_game_log_data = player_game_log.get_data_frames()[0]

ovrCounter = 0

ovrArr = []

for x in range(len(player_game_log_data)):
    lineCheck = 0
    for stat in statList:
        lineCheck += player_game_log_data[stat].iloc[x]
    if lineCheck > line:
        ovrCounter = ovrCounter + 1
        ovrArr.append(lineCheck)


print("------------------------------------------------------------------------------------------------------------------------------------------")
print("| This season, " + playerName + " has gone over the line of " + str(line) + " " + str(statsNeeded) + " " + str(ovrCounter) + " times in " + str(len(player_game_log_data) - 1) + " games")
print(ovrArr)
# Display the player's box scores


#-----------------------------------------------Code Graveyard------------------------------------------------------------

# url = "https://api-nba-v1.p.rapidapi.com/players"

# querystring = {}

# headers = {
# 	"X-RapidAPI-Key": "dc1dbb148emsh667601f198be67bp12c8a8jsnbd71fa52dcdc",
# 	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
# }

# playerName = input("Enter the player's last name: ")
# querystring['name'] = playerName

# response = requests.get(url, headers=headers, params=querystring)

# if (response.json()['results'] < 1):
#     print("No results found for this player!")
# elif (response.json()['results'] == 1):
#     querystring['id'] = response.json()['response'][0]['id']
#     del querystring['name']
#     print(querystring)