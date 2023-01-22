import os
import time

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

count = 0
for tweet in tweepy.Cursor(
    api.search_tweets,
    "#osm OR #openstreetmap OR #OSM OR #OPENSTREETMAP OR #HOTOSM OR #hotosm filter:nativeretweets exclude:retweets",
    count=100,
    tweet_mode="extended",
).items():
    try:
        api.retweet(tweet.id)
        print(f"Retweeted tweet by {tweet.user.screen_name}")
        time.sleep(2)
        count = count + 1
    except tweepy.errors.TweepyException as e:
        print(e.api_messages)
    except StopIteration:
        print("breaking")
        break
print(f"Retweeted {count} tweets")
