import snscrape.modules.twitter as sntwitter 
import pandas as pd 

query = "python"

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet)) #use vars to print all attributes of a tweets
    break 