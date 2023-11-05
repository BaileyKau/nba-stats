from nba_api.stats.endpoints import playercareerstats, teamvsplayer
from nba_api.stats.static import players, teams

playerName = input("Enter the player's full name: ")
# teamName = input("Enter the opposing team: ")

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

print("------------------------------------------------------------")
print("| All time, " + playerName + " has: \n|")
allTimeAvg = round(allTimeStat/gamesPlayed, 2)
print("| " + str(allTimeStat) + " " + statsNeeded + " in " + str(gamesPlayed) + " games to average " + str(allTimeAvg) + " " + statsNeeded)

print("------------------------------------------------------------")
print("| This season, " + playerName + " has: \n|")
thisSeasonAvg = round(thisSeasonStat/gamesPlayedThisYear, 2)
print("| " + str(thisSeasonStat) + " " + statsNeeded + " in " + str(gamesPlayedThisYear) + " games to average " + str(thisSeasonAvg) + " " + statsNeeded)
print("------------------------------------------------------------")


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