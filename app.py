import os

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Search for tweets containing either #osm or #openstreetmap
tweets = api.search_recent_tweets(
    q="#osm OR #openstreetmap OR #OSM OR #openmapping OR #OPENSTREETMAP OR #HOTOSM OR #hotosm",
)

# Retweet each tweet that was found
for tweet in tweets:
    try:
        api.retweet(tweet.id)
        print(f"Tweeted {tweet.id}")
    except Exception as e:
        print(e)
