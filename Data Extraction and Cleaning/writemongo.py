import pymongo
import json
#Insert raw tweets from json file into AWS Mongodb Instance
client = pymongo.MongoClient("mongodb://tester:password@ec2-3-85-20-108.compute-1.amazonaws.com/test")
db = client.test
with open('tweetStream25_950.json') as f:
    for idx, line in enumerate(f):
        if line != '\n':
            data = (json.loads(line))
            db.raw_tweets.insert(data)
