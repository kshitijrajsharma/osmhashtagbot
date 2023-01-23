import json
import os

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

# Load previously retweeted tweet IDs from JSON file
try:
    with open("meta.json", "r") as file:
        retweeted_tweets = json.load(file)
except:
    retweeted_tweets = []

count = 0
tweet_add_list = 0
# print(api.me())
for tweet in tweepy.Cursor(
    api.search_tweets,
    "#openstreetmap OR #osm OR #hotosm -filter:retweets",
    count=100,
).items():
    print(f"Going over tweet by {tweet.user.screen_name}")

    try:

        if not tweet.retweeted:
            # time.sleep(2)
            if tweet.id not in retweeted_tweets:
                api.retweet(tweet.id)
                print(f"Retweeted tweet by {tweet.user.screen_name}")
                retweeted_tweets.append(tweet.id)
                count = count + 1

    except tweepy.errors.TweepyException as e:
        error_msg = str(e)
        if "You have already retweeted this Tweet" in error_msg:
            retweeted_tweets.append(tweet.id)
            print("Added to retweeted list")  #
            tweet_add_list = tweet_add_list + 1
        else:
            print("Other Error Occured: ", error_msg)
        # break
# print(api.rate_limit_status())
with open("meta.json", "w") as file:
    json.dump(retweeted_tweets, file)

print(f"Retweeted {count} tweets , Added {tweet_add_list} to retweet list")
