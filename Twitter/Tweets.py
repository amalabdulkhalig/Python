import snscrape.modules.twitter as sntwitter 
import pandas as pd 
import arabic_reshaper as arabic


#query used like the Twitter serch bar, a single word could be searched or 
#you can use the advance serch then copy the query and paste it here as a text 
class Tweets:
    def __init__(self):
        self.query = "query" #"(from:elonmusk) until:2022-06-16 since:2020-01-01" 
        self.tweets = list() #save the list of tweets returns 
        self.limit = 10 #number of tweets returned 
    
    #-------------------------- 
    def GetNumTweets(self):
        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():
            if len(self.tweets) == self.limit:
                break 
            else:
                self.tweets.append([tweet.date,tweet.user.username,tweet.content])
        df = pd.DataFrame(self.tweets,columns=['Date','User','Tweet'])
        print(df['Tweet'][:1])
        return df

    def GetTweets(self):
        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():
            self.tweets.append([tweet.date,tweet.user.username,tweet.content])
        df = pd.DataFrame(self.tweets,columns=['Date','User','Tweet'])
        return df
    #--------------------------
    def GetNumArabicTweets(self):
        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():
            if len(self.tweets) == self.limit:
                break 
            else:
                reshaped_tweet = arabic.reshape(tweet.content)[::-1]
                self.tweets.append([tweet.date,tweet.user.username,reshaped_tweet])

        df = pd.DataFrame(self.tweets,columns=['Date','User','Tweet'])
        print(df['Tweet'][:1])
        return df

    #--------------------------
    def TestOneTweet(self):
        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():
            print(vars(tweet)) #use vars to print all attributes of a tweets
            break