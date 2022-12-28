import os

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuth1UserHandler(
    os.environ.get(consumer_key),
    os.environ.get(consumer_secret),
    os.environ.get(access_token),
    os.environ.get(access_token_secret),
)
api = tweepy.API(auth)

# Search for tweets containing either #osm or #openstreetmap
tweets = api.search(q="#osm OR #openstreetmap OR #OSM OR #OPENSTREETMAP", lang="en")

# Retweet each tweet that was found
for tweet in tweets:
    api.retweet(tweet.id)
