import os
import time

import tweepy

# Authenticate using your API keys and access tokens
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth, wait_on_rate_limit=True)

# Get rate limit status
rate_limit_status = api.rate_limit_status()

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

count = 0
# Search for tweets
tweets = tweepy.Cursor(
    api.search_tweets,
    q="#openstreetmap #hotosm -filter:retweets",
    count=100,
    tweet_mode="extended",
).items()
print(tweets)

# Retweet the tweets
for tweet in tweets:
    print(tweet)
    if (
        api.rate_limit_status()["resources"]["statuses"]["/statuses/retweet/:id"][
            "remaining"
        ]
        == 0
    ):
        print("I have reached the rate limit for this endpoint.")
        break
    else:
        api.retweet(tweet.id)
        count = count + 1
        print(f"Retweeted tweet by {tweet.user.screen_name}")

print(f"Retweeted {count} tweets")
