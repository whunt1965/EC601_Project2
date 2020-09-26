# EC601_Project2
Repository for EC601 Project2 in which I explore uses of the Twitter API and Google NLP API

## Contents

### Google_NLP
Provides a few simple test programs for using the Google NLP API, including:
* **NLP_cl.py** - A simple program which allows a user to enter input via the command line and view the resulting sentiment analysis (sentiment score and magnitude) of the input.
* **NLP_txt.py** - A program which allows users to upload a .txt file and perform sentiment analysis on the document. The program also allows users to optionally also perform   sentiment analysis on each line in the file. 
* **NLPTest.txt** - A sample .txt file which can be analyzed via NLP_txt.py.

### Twitter_API
Provides example programs showcasing a few capabilities of the Twitter API (using [Tweepy](https://github.com/tweepy/tweepy)), including:
* **keyword_query.py** - A program which extracts text content from tweets containing a user-defined keyword (eg, a Twitter handle) and stores it in an ouput file (such as a .txt file).
* **timeline_query.py** - A program which extracts statuses from a specified twitter user and allows users to export the status objects into a JSON file and/or extract the status text content and export it into a .txt file.
* **twitter_trends.py** -- A program which allows users to extract the top trends on Twitter, either globally or using a specific WOEID (Where on Earth Identifier), and export the trends into a .txt file and a JSON file. 

### POCs
A pair of test programs utilizing a common POCEngine.py file which to extract tweets (via the Twitter API) based on a given input and analyze sentiment via the Google NLP API.
* **PocEngine.py** - A program which takes in a given keyword (e.g. a Twitter Handle), retrieves the n most recent tweets with that term, and then processes the text of each tweet using the Google NLP API. The program returns a "score" representing the overall sentiment surrouding that keyword as well as the "Most Positive" and "Most Negative" tweets analyzed in which that keyword is used. 
* **MiseryIndex.py** - Inspired by [ESPN's College Football Fan Happiness Index](https://www.espn.com/college-football/story/_/id/21342892/college-football-fan-happiness-index-november-2017-update), this simple program determine which College Football (or other) fanbase is most miserable! This program uses the PocEngine to analyze official College Football team Twitter handles and provides a ranking of most miserable to least based on tweet sentiment analysis. While designed for college football fan bragging rights, this program could really be used to rank sentiment around any number of organizations
* **HeatCheck.py** -Which coach is on the hot seat today? This program uses the PocEngine to analyze the sentiment tweets tagging a college football coach's Twitter handle and returns a ranking of least-positive (on the hot seat) to most positive.

## Prerequisites for Usage
### Google_NLP files
A [Google Cloud Platform](https://cloud.google.com) account is required to use the Google NLP API. Users should be sure to carefully follow the steps for setting up authorization prior to attempting to utilize these files. 
### Twitter_API files
A [Twitter Developer](https://developer.twitter.com/) account is required to use the Twitter API. In addition, users will need to follow the instructions to install Tweepy available on the [Tweepy GitHub Repository](https://github.com/tweepy/tweepy). To utilize the programs in this repository, users will need to add their own Twitter credentials (consumer key/secret and access key/secret) in the text blocks indicated in each file or via another mechanism.
### POCs
As the POCs use both the Google NLP and Twitter API's, users will need to follow the steps listed above to set up both Google Cloud Platform and Twitter Developer accounts.

## Acknowledgements
The code for the Twitter_API samples utilized an example provided by Professor Osama Alshaykh as a "jumping off" point to learn how to use the API. Meanwhile, the Google_NLP programs leveraged Google's [Quickstart: Using Client Libraries](https://cloud.google.com/natural-language/docs/quickstart-client-libraries#client-libraries-usage-python) as a foundational example.
