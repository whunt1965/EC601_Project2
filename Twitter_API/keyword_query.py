# Module extracts text from tweets based on a search query and stores it in 
# a specified file (eg, a .txt file)

import tweepy

#Twitter API credentials
# consumer_key = ""
# consumer_secret = ""
# access_key = ""
# access_secret = ""


def keyquery(tag, n=10, disallowRT=True, filename="tweets.txt"):
    
    #If we want to filter out RT from our results, concatenate filter onto query
    if disallowRT:
        tag = tag + "-filter:retweets"
    
    #authorize for Twitter and initialziation of Tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #Request n tweets for query
    alltweets = api.search(q = tag,count=n)
    
    #write tweet text to a .txt file
    file = open(filename, 'w') 
    print("Writing tweets to", filename)
    for tweet in alltweets:
        file.write(tweet.text)
        file.write('\n')
    
    #close the file
    print("Search finished! View results in", filename)
    file.close()

if __name__ == '__main__':
    # pass in keyword you want to search. You can also optionally, specify #tweets 
    # (n, default=10),output file name (filename, default=tweets.txt), and whether 
    # you want to exclude retweets in your query (disallowRT, default=True)
    keyquery(tag = "@Vol_Football")