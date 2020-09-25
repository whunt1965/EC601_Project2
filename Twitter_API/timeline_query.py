# Module extracts n most recent statuses from a specified user and allows:
# 1) status text to be put into a text file
# 2) Status objects to be exported to a JSON file

import tweepy
import json

#Twitter API credentials
# consumer_key = ""
# consumer_secret = ""
# access_key = ""
# access_secret = ""


#Requests n most recent statuses from a user and returns a list of "status objects"
def getRecentPosts(user, count):
    tweetHist = api.user_timeline(id = user,count=count) #request list from API
    return tweetHist #return list

#Exports content (text) of status to a .txt file
def exportTweetText(obj, filename = "out.txt"):   
    file = open(filename, 'w') 
    print("Writing tweets to", filename)
    for tweet in obj:
        file.write(tweet.text + '\n')
    print("File write complete. Tweets are available in", filename)
    file.close()

#Dumps tweetstatus objects into a JSON
def exportRecentPostJSON(obj, filename = "Tweets.json"):   
    file = open(filename, 'w') 
    for status in obj:
        json.dump(status._json,file,indent = 4)
    print("Export complete. Data is available in", filename)
    file.close()

if __name__ == '__main__':
    #authorizations and registrations
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #***Demo***#
    #requests 10 statuses from @CoachJPruitt
    myTweets = getRecentPosts(user = "@CoachJPruitt", count = 10)

    #Puts status text into a text file (user can specify filename or
    # default to "out.txt")
    exportTweetText(obj = myTweets, filename = "PruittTweets.txt")

    #Exports tweet status objects as a JSON (user can specify filename or default
    # to "Tweets.JSON")
    exportRecentPostJSON(obj = myTweets, filename = "PruittTweets.json")
