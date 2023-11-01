import http.client

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "dc1dbb148emsh667601f198be67bp12c8a8jsnbd71fa52dcdc"
    }

conn.request("GET", "/players?name=Devion Mitchell", headers=headers)

res = conn.getresponse()
data = res.read()

print(data)

# playerName = input("Enter the player's name: ")

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
