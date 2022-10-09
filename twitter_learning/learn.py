import tweepy
import twitter_credentials
auth = tweepy.OAuth1UserHandler(
   twitter_credentials.CONSUMER_KEY, 
   twitter_credentials.CONSUMER_SECRET ,
   twitter_credentials.ACCESS_TOKEN , 
   twitter_credentials.ACCESS_TOKEN_SECRET 
) 

api = tweepy.API(auth)
user = api.get_user(screen_name = 'twitter')
print(user.screen_name)
print(user.followers_count) 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)