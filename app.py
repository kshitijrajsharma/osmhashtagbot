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
for tweet in tweepy.Cursor(
    api.search_tweets,
    "#openstreetmap OR #osm OR #hotosm -filter:retweets",
    count=100,
).items():
    print(f"Going over tweet by {tweet.user.screen_name}")

    try:
        if (
            api.rate_limit_status()["resources"]["statuses"]["/statuses/retweets/:id"][
                "remaining"
            ]
            == 0
        ):
            print("I have reached the rate limit for this endpoint.")
            break
        if api.get_user().id not in tweet.retweeters:
            time.sleep(2)
            api.retweet(tweet.id)
            print(f"Retweeted tweet by {tweet.user.screen_name}")
            count = count + 1

    except Exception as e:
        print(api.rate_limit_status())
        print(e)
        break
# print(api.rate_limit_status()["resources"])
print(f"Retweeted {count} tweets")
