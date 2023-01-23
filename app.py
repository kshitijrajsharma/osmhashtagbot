import os
import time

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

print("started")
api = tweepy.API(auth)
# print(api.rate_limit_status()["resources"]["statuses"])
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

count = 0
# the screen name of the user
screen_name = "OSM_retweet_bot"

# fetching the user
user = api.get_user(screen_name)

# fetching the ID
ID = user.id_str

print("The ID of the user is : " + ID)
for tweet in tweepy.Cursor(
    api.search_tweets,
    "#openstreetmap OR #osm OR #hotosm -filter:retweets",
    count=100,
).items():
    print(f"Going over tweet by {tweet.user.screen_name}")

    try:
        if api.get_user().id not in tweet.retweeters:

            api.retweet(tweet.id)
            print(f"Retweeted tweet by {tweet.user.screen_name}")
            count = count + 1

    except Exception as e:
        print(e)
        break
print(api.rate_limit_status()["resources"])
print(f"Retweeted {count} tweets")
