# Import the tweepy library
import tweepy

# Specify your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter using your API credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get a list of the users you follow on Twitter
following = api.friends_ids()

# Get a list of users who follow you on Twitter
followers = api.followers_ids()

# Iterate through the list of users you follow
for user_id in following:
  # Check if the user does not follow you
  if user_id not in followers:
    # Unfollow the user
    api.destroy_friendship(user_id)
