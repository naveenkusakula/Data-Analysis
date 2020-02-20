# Tweets ETL

#### Cluster Setup:
AWS EC2 Instance that already created during the lab is used. Spark with a master and a slave is
initialized to run MapReduce jobs. Mongo DB is installed on the same cloud instance, the tweets
and corresponding metadata are stored in Mongo DB.
#### Data Extraction & Transformation: (Python is used for the assignment)
##### Twitter API Exploration:
Twitter development account Datawarehousing_Dalhousieuniversity and Assignment2_Data
(16128177) application, used as to search and stream tweets from twitter. The response from
the search api contains recent tweets in past 7 days and only public tweets, as the account used
is standard and not premium. Real time tweets and retweets are streamed when Stream api is
used. The twitter api response is json and contains the actual full tweet text if streamed /
searched in extended mode, if not in extended mode then some of the tweet text might be
truncated. It contains user information, details about user location, retweeted status, user
mentions, etc.
##### Twitter sample JSON data:
{"contributors": null, "truncated": false, "is_quote_status": false, "in_reply_to_status_id": null,
"id": 1100302009037668352, "favorite_count": 0, "full_text": "Car park South has 50 spaces
coned off today and tomorrow. Due to events happening. The rest of the car park is open as
normal. If full when you arrive please park in Sports Centre, car park West, Halifax College, car
park North, Central car park", "entities": {"symbols": [], "user_mentions": [], "hashtags": [],
"urls": []}, "retweeted": false, "coordinates": null, "source": "<a
href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
"in_reply_to_screen_name": null, "in_reply_to_user_id": null, "display_text_range": [0, 246],
"retweet_count": 0, "id_str": "1100302009037668352", "favorited": false, "user":
{"follow_request_sent": false, "has_extended_profile": false, "profile_use_background_image":
true, "default_profile_image": false, "id": 2858500305, "profile_background_image_url_https":
"https://abs.twimg.com/images/themes/theme1/bg.png", "verified": false, "translator_type":
"none", "profile_text_color": "333333", "profile_image_url_https":
"https://pbs.twimg.com/profile_images/930719101835792384/7Zvrktf9_normal.jpg",
"profile_sidebar_fill_color": "DDEEF6", "entities": {"description": {"urls": []}}, "followers_count":
256, "profile_sidebar_border_color": "C0DEED", "id_str": "2858500305",
"profile_background_color": "C0DEED", "listed_count": 7, "is_translation_enabled": false,
"utc_offset": null, "statuses_count": 4969, "description": "Availability of parking bays around
the University of York.", "friends_count": 3, "location": "", "profile_link_color": "1DA1F2",
"profile_image_url":
"http://pbs.twimg.com/profile_images/930719101835792384/7Zvrktf9_normal.jpg",
"following": false, "geo_enabled": true, "profile_background_image_url":
"http://abs.twimg.com/images/themes/theme1/bg.png", "screen_name": "UoYParkingBays",
"lang": "en", "profile_background_tile": false, "favourites_count": 8, "name": "Parking Bays",
"notifications": false, "url": null, "created_at": "Mon Nov 03 09:14:03 +0000 2014",
"contributors_enabled": false, "time_zone": null, "protected": false, "default_profile": true,
"is_translator": false}, "geo": null, "in_reply_to_user_id_str": null, "lang": "en", "created_at":
"Tue Feb 26 07:50:16 +0000 2019", "in_reply_to_status_id_str": null, "place": null, "metadata":
{"iso_language_code": "en", "result_type": "recent"}}
#### Data Extraction:
ExtractTweets.py is used to extract tweets using Search API, the responses are stored as json
objects in tweetSearch_.json files, approximately 600 - 700 Tweets are extracted.
Stream.py is used to stream real time tweets using Stream API, the responses are stored as json
objects in tweetsstream_timestamp.json, streaming was ran at different times approximately to
get 200 tweets each time and a total of approximately 1200 tweets are extracted.
writemongo.py is used to insert tweets to mongodb running in the cloud instance in raw_tweets
collection.
#### Transformation:
Cleantweets.py is used to get text from raw tweets, raw tweet objects in json file are read and
tweet text alone is extracted from the json objects, then emoticons are removed by changing
the string from Unicode to latin-1 character set, also all special characters are removed from the
tweet text and finally wrote into tweettext.txt file, which contains tweet text alone. This file is
uploaded into EC2 instance for processing.
#### Data Processing (Map Reduce)
PYSpark is used to perform Map Reduce on tweettext.txt (Cleaned file with approx. 1600
tweets), there are three simple applications created for counting the occurrences of the given
keywords and keystrings
1. Pattern.py – This app is used to count keystrings like “good schools” in the tweettext.txt
and stores count in output file
2. Exactmatch.py – This app is used to count keywords like “safe’ in the tweettext.txt and
stores count in output file
3. Count.py – Count all the words count in the tweettext.txt
and stores count in output file

# SENTIMENTANALYSIS

1. SentimentAnalysis.py - Perform Sentiment Analysis on the extracted tweets and determine the polarity
2. SimanticAnalysis.py - Perform Simantic Analysis on the extracted tweets using IDF and rank the 
