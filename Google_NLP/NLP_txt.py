# Simple program using Google NLP to analyze sentiment of a document
# Provides sentiment analysis for document as a whole as well as
# the possibility to analyze each line of the document independently

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Function analyzes user input and outputs sentiment score and magnitude
def analyzeline(userline, client):
    # The text to analyze
    text = userline

    #create document
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text and prints results
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print("Line: {}".format(text))
    print ("Sentiment score:  {}. Sentiment Magnitude:  {}".format(sentiment.score, sentiment.magnitude))


def analyzedoc(filename, client):
    # Open the file and read text
    text = ""
    with open(filename, 'r') as f1:
        text = f1.read()
    f1.close()

    #create document
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text and prints results
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print ("Document Sentiment score:  {}".format(sentiment.score))
    print ("Document Sentiment Magnitude:  {}".format(sentiment.magnitude))

    #Optionally allow line by line analysis
    linebyline = input("Would you like an analysis for each line of the document (Y/N)?")
    if linebyline == 'Y':
        lines = []
        with open(filename, 'r') as f1: #read lines into a list
            lines = f1.readlines()
        f1.close()
        for line in lines: #call analyzline method on each line
            analyzeline(userline=line.strip(), client=client)

if __name__ == '__main__':
    # Instantiates a client
    client = language.LanguageServiceClient()
    #Runs analysis on a given file 
    analyzedoc(filename = "NLPTest.txt", client=client)
