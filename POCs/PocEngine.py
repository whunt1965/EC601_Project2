# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Imports Tweepy and sets credentials
import tweepy

#Twitter API credentials
#Twitter API credentials
# consumer_key = ""
# consumer_secret = ""
# access_key = ""
# access_secret = ""

def calc_score(handle):

    #authorize for Twitter and initialziation of Tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Instantiates GoogleNLP client
    client = language.LanguageServiceClient()

    #disallow retweets
    handle = handle + "-filter:retweets"

    #Vars encapsulating key attributes of each handle:
    rawscore = 0 #Raw score for handle
    mostpos = "" #most positive tweek
    mpscore = float("-INF") #associated score for most positive tweet
    mostneg = "" #most negative tweet
    mnscore = float("INF") #associated score for most negative tweet
    
    #Request 10 tweets for query
    tweets = api.search(q = handle,count=10)
    
    #Iterate through tweets and process
    for tweet in tweets:

        #Extract text
        text = tweet.text 

        #Perform NLP processing
        document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        #calc score and add to raw score
        score = sentiment.score * sentiment.magnitude
        rawscore += score

        #update most postive and most negative tweets
        if score > mpscore:
            mpscore = score
            mostpos = text.strip()
        if score < mnscore:
            mnscore = score
            mostneg = text.strip()

    return (rawscore, mostpos, mostneg)


    

