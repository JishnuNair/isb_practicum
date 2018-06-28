from TwitterSearch import *
import datetime
import os
import glob
import pandas as pd

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

coinmarket_path='/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/daily_data'
with cd(coinmarket_path):
    latest_file = max(glob.iglob('ticker_*'), key=os.path.getctime)

latest_file = os.path.join(coinmarket_path,latest_file)
# print(latest_file)

ticker_df = pd.read_csv(latest_file)
keywords = list(ticker_df.iloc[:3,5])
keywords = [keyword.lower() for keyword in keywords]
print(keywords)

now = datetime.datetime.now()

for keyword in keywords:
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([keyword],or_operator=True) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see english tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

        # Creating a TwitterSearch object with secret tokens
        ts = TwitterSearch(
            consumer_key = '<>',
            consumer_secret = '<>',
            access_token = '<>',
            access_token_secret = '<>'
         )

         # Pulling data using TwitterSearch library
        with open('/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/daily_data/{0}_tweets_{1}'.format(keyword,datetime.datetime.today().strftime('%Y%m%d')),'w') as fileout:
            #for tweet in ts.search_tweets_iterable(tso):
            #    fileout.write('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            for idx,tweet in enumerate(ts.search_tweets_iterable(tso)):
                fileout.write('###TWEET_NO:%d###!###USER:%s###!###DATE_TIME:%s###!###LOCATION:%s###!###TWEET:%s' % ( idx,tweet['user']['screen_name'],tweet['created_at'],tweet['user']['location'],tweet['text'] ) )
                fileout.write('\n')

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)
