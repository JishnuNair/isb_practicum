
# coding: utf-8

# In[1]:
import requests
import pandas as pd
import datetime
from pandas.io.json import json_normalize

response = requests.get('https://api.coinmarketcap.com/v2/listings/')
data = response.json()
listings = pd.DataFrame(data['data'])

ticker_df = pd.DataFrame()

try:
    for listing_id in range(1,listings.id.max(),100):
        response = requests.get('https://api.coinmarketcap.com/v2/ticker/?start={0}&sort=id&structure=array'.format(listing_id))
        new_data = json_normalize(response.json()['data'])
        ticker_df = ticker_df.append(new_data,ignore_index=True)
except:
    pass

response = requests.get('https://api.coinmarketcap.com/v2/global/')
global_data = json_normalize(response.json()['data'])

now = datetime.datetime.now()

ticker_df = ticker_df.sort_values(by='rank')

listings.to_csv('/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/listings_{0}.csv'.format(str(now.strftime("%Y%m%d"))))
ticker_df.to_csv('/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/ticker_data_{0}.csv'.format(str(now.strftime("%Y%m%d"))))
global_data.to_csv('/home/jishnu/Documents/ISB/Term3/practicum/workspace/data_collection/data/global_data_{0}.csv'.format(str(now.strftime("%Y%m%d"))))

