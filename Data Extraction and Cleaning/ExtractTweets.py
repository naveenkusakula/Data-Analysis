import tweepy
import json


raw_file = open("tweetSearch2.json", "w")

#Authenticate method to connect to twitter API
def authentication():
    con_key = 'hDRwqboDuZaPBdhDQg9kvdpdz'
    con_secret = 'ix1ubBeHHJFeO2a7FMsbNAuHiWQWJs2QJ0k0Nxqlj1HTwRo2FA'
    acc_key = '1095013945931370501-mFRIyafZ3PJxXvF6mZGzlHdwCVTKg6'
    acc_secret = 'bF8WLR11g5kpb7uppac9YHmCioU3MJxmeKZ8sx67WYNlR'

    auth = tweepy.auth.OAuthHandler(con_key, con_secret)
    auth.set_access_token(acc_key, acc_secret)
    return tweepy.API(auth)

#Extract 100 tweets using Search API and write json objects to output file
def extractsearch():
    api = authentication()
    raw_tweets = api.search(q="halifax", count=100, tweet_mode="extended")
    for i in raw_tweets:
        tweetobj = json.dumps(i._json)
        raw_file.write(tweetobj + '\n')
    print "tweets extracted"

#twice to get more tweets
extractsearch()
extractsearch()
