from Tweets import Tweets

results = Tweets()
results.query = "deep learning machine learning AI (machine OR deep OR learning OR AI OR ML OR DL) until:2022-06-16 since:2022-05-16"
tweets = results.GetTweets()
#tweets.to_csv("TweetsCSV.csv", index=False,columns=['Date','User','Tweet'])
tweets