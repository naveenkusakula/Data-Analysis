import tweepy
import json

raw_file = open("TaskD.json", "w")

#Authenticate method to connect to twitter API
def authentication():
    con_key = 'hDRwqboDuZaPBdhDQg9kvdpdz'
    con_secret = 'ix1ubBeHHJFeO2a7FMsbNAuHiWQWJs2QJ0k0Nxqlj1HTwRo2FA'
    acc_key = '1095013945931370501-mFRIyafZ3PJxXvF6mZGzlHdwCVTKg6'
    acc_secret = 'bF8WLR11g5kpb7uppac9YHmCioU3MJxmeKZ8sx67WYNlR'

    auth = tweepy.auth.OAuthHandler(con_key, con_secret)
    auth.set_access_token(acc_key, acc_secret)
    return tweepy.API(auth)

#write real time tweets to json file
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweetobj = json.dumps(status._json)
        print(tweetobj)
        raw_file.write(tweetobj + '\n')

#method to stream tweets in real time
def extractstream():
    api = authentication()
    stream = MyStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream, tweet_mode="extended")
    stream.filter(track=['halifax'])


extractstream()
