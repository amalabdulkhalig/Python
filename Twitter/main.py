from Tweets import Tweets

results = Tweets()
results.query = 'Python'
tweets = results.GetTweets()
print(tweets)
tweets.to_csv("TweetsCSV", encoding='utf-8', index=False,columns=['Date','User','Tweet'])