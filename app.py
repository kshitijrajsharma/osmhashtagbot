import os

import tweepy

bearer_token = os.environ["BEARER_TOKEN"]

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]

access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)
# Search for tweets containing either #osm or #openstreetmap

response = client.search_recent_tweets(
    "#osm OR #openstreetmap OR #OSM OR #OPENSTREETMAP OR #HOTOSM OR #hotosm",
    max_results=100,
)

# Retweet each tweet that was found
for tweet in response:
    try:
        client.retweet(tweet.id)
        print(f"Retweeted {tweet.id}")
    except Exception as e:
        print(e)
