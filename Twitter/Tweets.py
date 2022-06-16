import snscrape.modules.twitter as sntwitter 
import pandas as pd 
import arabic_reshaper as arabic

#query used like the Twitter serch bar, a single word could be searched or 
# you can use the advance serch then copy the query and paste it here as a text 
class Twitter:
    def __init__(self, query: str, limit: int) -> None:
        self.query = query #"(from:elonmusk) until:2022-06-16 since:2020-01-01" 
        self.tweets = [] #save the list of tweets returns 
        self.limit = limit #10 #number of tweets returned 

    def GetTweets(query):
        # vars(tweets) returns a dictionary of the tweets any it's metadata 
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            #print(vars(tweet)) #use vars to print all attributes of a tweets
            #break 
            if len(tweets) == limit:
                break 
            else:
                reshaped_tweet = arabic.reshape(tweet.content)[::-1]
                tweets.append([tweet.date,tweet.user.username,reshaped_tweet])

        df = pd.DataFrame(tweets,columns=['Date','User','Tweet'])
        print(df['Tweet'][:1])


    def GetArabicTweets(query):
        # vars(tweets) returns a dictionary of the tweets any it's metadata 
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            #print(vars(tweet)) #use vars to print all attributes of a tweets
            #break 
            if len(tweets) == limit:
                break 
            else:
                reshaped_tweet = arabic.reshape(tweet.content)[::-1]
                tweets.append([tweet.date,tweet.user.username,reshaped_tweet])

        df = pd.DataFrame(tweets,columns=['Date','User','Tweet'])
        print(df['Tweet'][:1])

    #--------------------------

    def testOneTweet(query):
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            print(vars(tweet)) #use vars to print all attributes of a tweets
            break