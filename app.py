import os
import time

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth, wait_on_rate_limit=True)
print(api.rate_limit_status())
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

count = 0
for tweet in tweepy.Cursor(
    api.search_tweets,
    "#openstreetmap -filter:retweets",
    count=300,
).items():

    try:
        if (
            api.rate_limit_status()["resources"]["statuses"]["/statuses/retweet/:id"][
                "remaining"
            ]
            == 0
        ):
            print("I have reached the rate limit for this endpoint.")
            break
        api.retweet(tweet.id)
        print(f"Retweeted tweet by {tweet.user.screen_name}")
        count = count + 1
        time.sleep(2)
    except Exception as e:
        print(e)
print(f"Retweeted {count} tweets")
