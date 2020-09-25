# Simple test POC to see which coach is on the hot seat! Uses Twitter API to 
# extract tweets at a coach's handle and then provides a score based on Google NLP
# sentiment analysis of Tweets

import PocEngine as pe

#Dummy list of 3 SEC coaches
coaches = [
    {"name": "Jeremy Pruitt", "Uni": "Tennessee", "handle": "@CoachJPruitt", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Derek Mason", "Uni": "Vanderbilt", "handle": "@CoachDerekMason", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Will Muschamp", "Uni": "South Carolina","handle": "@CoachWMuschamp", "score": 0, "mostpos": "", "mostneg": ""}
]
    
#Iterate through list and store data
for coach in coaches:
    (coach["score"], coach["mostpos"], coach["mostneg"]) = pe.calc_score(coach["handle"])
    
#sort list by score
coaches.sort(key=lambda x: x['score'])
    
#Print Heat Check and analysis
print("Processing data. This could take a moment...")
print()
print("*** Heat Check! ***")
print()
i = 1
for coach in coaches:
    print("{}: {}, {}".format(i, coach["name"], coach["Uni"]))
    print("     Score: {}".format(coach["score"]))
    print("     Most Positive Tweet: {}".format(coach["mostpos"].replace("\n", " ")))
    print("     Most Negative Tweet: {}".format(coach["mostneg"].replace("\n", " ")))
    i += 1
    print()

