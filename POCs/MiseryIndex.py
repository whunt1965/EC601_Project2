# Simple test POC to see which team's fanbase is the most miserable! Uses Twitter API to 
# extract tweets at a team's handle and then provides a score based on Google NLP
# sentiment analysis of Tweets

import PocEngine as pe

#Dummy list of 3 SEC teams
teams = [
    {"name": "Tennessee Volunteers", "handle": "@Vol_Football", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Vanderbilt Commodores", "handle": "@VandyFootball", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "South Carolina Gamecocks", "handle": "@GamecockFB", "score": 0, "mostpos": "", "mostneg": ""}
]
    
#Iterate through list and store data
for team in teams:
    (team["score"], team["mostpos"], team["mostneg"]) = pe.calc_score(team["handle"])
    
#sort list by score
teams.sort(key=lambda x: x['score'])
    
#Print Misery Index and analysis
print("Processing data. This could take a moment...")
print()
print("*** Misery Index! ***")
print()
i = 1
for team in teams:
    print("{}: {}".format(i, team["name"]))
    print("     Score: {}".format(team["score"]))
    print("     Most Positive Tweet: {}".format(team["mostpos"].replace("\n", " ")))
    print("     Most Negative Tweet: {}".format(team["mostneg"].replace("\n", " ")))
    i += 1
    print()

