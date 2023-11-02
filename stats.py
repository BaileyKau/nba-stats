from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

playerName = input("Enter the player's name: ")

player = players.find_players_by_full_name(playerName)
playerID = player[0]['id']
career = playercareerstats.PlayerCareerStats(player_id=playerID) 

# print("JSON: " + career.get_json())
# print(career.get_dict())

# Data Frame [0] is the season by season breakdown of statistics 
# Data Frame [1] is the all time totals
print(career.get_data_frames())

# statsNeeded = input("""\nAbbreviations:\n
# 'P' Points\n           
# 'R' Rebounds\n      
# 'A' Assists\n       
# 'S' Steals\n        
# 'B' Blocks\n        
# 'FP' Fantasy Points\n
# 'P+R' Pts + Rebs\n
# 'TO' Turnovers\n
# Enter the statistic needed: """)




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