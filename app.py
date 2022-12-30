import os

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuthHandler(os.environ.get("API_KEY"), os.environ.get("API_KEY_SECRET"))
auth.set_access_token(
    os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET")
)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Search for tweets containing either #osm or #openstreetmap
tweets = api.search_tweets(
    q="#osm OR #openstreetmap OR #OSM OR #OPENSTREETMAP", lang="en"
)

# Retweet each tweet that was found
for tweet in tweets:
    print(f"Retweeting {tweet.id}")
    api.retweet(tweet.id)
