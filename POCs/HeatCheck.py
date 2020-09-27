# Simple test POC to see which coach is on the hot seat! Uses Twitter API to 
# extract tweets at a coach's handle and then provides a score based on Google NLP
# sentiment analysis of Tweets

import PocEngine as pe

#Dummy list of 3 SEC coaches
coaches = [
    {"name": "Jeremy Pruitt", "Uni": "Tennessee", "handle": "@CoachJPruitt", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Derek Mason", "Uni": "Vanderbilt", "handle": "@CoachDerekMason", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Will Muschamp", "Uni": "South Carolina","handle": "@CoachWMuschamp", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Dan Mullen", "Uni": "Florida","handle": "@CoachDanMullen", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Mark Stoops", "Uni": "Kentucky","handle": "@UKCoachStoops", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Eliah Drinkwitz", "Uni": "Missouri","handle": "@CoachDrinkwitz", "score": 0, "mostpos": "", "mostneg": ""},
    {"name": "Kirby Smart", "Uni": "Georgia","handle": "@KirbySmartUGA", "score": 0, "mostpos": "", "mostneg": ""},
]

#number of tweets fetched per coach
tweetnumber = 40

#Message to user. Processing takes a minute
print("Processing data. This could take a moment...")
print()
#Iterate through list and store data
for coach in coaches:
    (coach["score"], coach["mostpos"], coach["mostneg"]) = pe.calc_score(coach["handle"], tweetcount = tweetnumber)
    
#sort list by score
coaches.sort(key=lambda x: x['score'])
    
#Print Heat Check and analysis
print("*** SEC EAST Coaches Hot Seat Ranking! ***")
print()
i = 1
for coach in coaches:
    if i == 1:
        print("{}: {}, {} (On the Hot Seat!)".format(i, coach["name"], coach["Uni"]))
    elif i == len(coaches):
        print("{}: {}, {} (Looks Safe! For now...)".format(i, coach["name"], coach["Uni"]))
    else:
        print("{}: {}, {}".format(i, coach["name"], coach["Uni"]))
    print("     Score: {}".format(coach["score"]))
    print("     Most Positive Tweet: {}".format(coach["mostpos"].replace("\n", " ")))
    print("     Most Negative Tweet: {}".format(coach["mostneg"].replace("\n", " ")))
    i += 1
    print()

