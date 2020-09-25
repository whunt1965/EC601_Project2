# Simple command line program using Google NLP to analyze sentiment of
# user input. Format based on Google NLP "hello world" tutorial

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Function analyzes user input and outputs sentiment score and magnitude
def anlyzetext(usertext):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text = usertext
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    #Prints results
    print('You entered: {}'.format(text))
    print ("Your Sentiment score:  {}".format(sentiment.score))
    print ("Your Sentiment Magnitude:  {}".format(sentiment.magnitude))

if __name__ == '__main__':
    while True:
        text = input("Please enter some text. Enter 'quit' to quit: ")
        if text == 'quit':
            break
        anlyzetext(text)

