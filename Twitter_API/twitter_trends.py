# Module provides an interface to extract twitter trends either globally or 
# at a specific location. These are put into a .txt file and optionally
# can also be put into a JSON

import tweepy
import json

#Twitter API credentials
# consumer_key = ""
# consumer_secret = ""
# access_key = ""
# access_secret = ""

#Extracts top 50 global trending topics and lists them in a txt file
#User can also optionalluy export a JSON
def getGlobalTrends(api, filename = "globalTrends.txt", exportJSON = False, JSONfilename = "globalTrends.json"):
    trends = api.trends_place(1) #extract JSON object of trends. 1 is the global ID.Re
    trendlist = trends[0]['trends'] #parse object to just extract list of trends dictionary objects
    file = open(filename, 'w') #write trends to filre 
    for trend in trendlist:
        file.write(trend["name"] + '\n')
    print("Trend Extraction complete. Data is available in", filename)
    file.close()

    #optionally allows a user to dump all trends data into a JSON file
    if exportJSON:
        file = open(JSONfilename, 'w') 
        json.dump(trends, file, indent = 4)
        print("JSON Export complete. Data is available in", JSONfilename)
        file.close()

#Extracts top local trending topics for a given WOEID and lists them in a txt file
#User can also optionally export a JSON
def getLocalTrends(api, id, filename = "localTrends.txt", exportJSON = False, JSONfilename = "localTrends.json"):
    trends = api.trends_place(id) #extract JSON object of trends based on user-defined WOEID
    trendlist = trends[0]['trends'] #parse object to just extract list of trends dictionary objects
    file = open(filename, 'w') #write trends to file 
    for trend in trendlist:
        file.write(trend["name"] + '\n')
    print("Trend Extraction complete. Data is available in", filename)
    file.close()

    #optionally allows a user to dump all trends data into a JSON file
    if exportJSON:
        file = open(JSONfilename, 'w') 
        json.dump(trends, file, indent = 4)
        print("JSON Export complete. Data is available in", JSONfilename)
        file.close()

if __name__ == '__main__':
    #authorizations and registrations
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #Get global trends and export text to .txt file (and optionally JSON)
    # Func Signature:
    # getGlobalTrends(api, filename = "globalTrends.txt", exportJSON = False, JSONfilename = "globalTrends.json"):
    getGlobalTrends(api=api, exportJSON=False)

    #Get Local Trends and export text to .txt file (and optionally JSON)
    # Func Signature:
    # def getLocalTrends(api, id, filename = "localTrends.txt", exportJSON = False, JSONfilename = "localTrends.json"):
    getLocalTrends(api=api, id=2442047, exportJSON=False)# 2442047 is the WOEID for NY 
