import tweepy
import datetime
from googlesearch import search


class Twitter:
	def __init__(self, tweet, tweet_date, tweet_time, profile_image_url):
		self.tweet = str(tweet)
		self.tweet_date = str(tweet_date)
		self.tweet_time = str(tweet_time)
		self.profile_image_url = str(profile_image_url)

	def __repr__(self):
		return f'{self.tweet} -- {self.tweet_date} -- {self.profile_image_url}'

def get_screen_name(face_name):

# to search
	query = face_name.lower() + " twitter screen name"
	res = search(query, tld="co.in", num=10, stop=10, pause=2)

	link = ''

	# for j in res:
	# 	print(j)

	for j in res:
		if str(j).find('twitter') != -1:
			link = j
		# print(j)
			break
	lst = link.split('/')
	screen_name = lst[len(lst)-1]
	pos = screen_name.find('?')
	if pos != -1:
		screen_name = screen_name[:pos]
	# print(screen_name)
	return screen_name

def get_tweets(user_screen_name):
	# Initialize twitter account credentials
	consumer_key = "82ZBWN7VF93E2PxiduNJxFt5b"
	consumer_secret = "1BdNAkCIqmsUPCvc0fZH9yVl94Im7W26JSRgzxUgC3p0uM09Yh"
	access_token = "3189799836-LN5NMDrrsoF8kfdgM4Np6IRADIO8bow7jgUuLtf"
	access_token_secret = "TzDR6idvO6SkTrbB5lkf83e8hPv7kUuYRsq7X3UkIM5Mc"

	# connect with twitter API by tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)

	tweets = api.user_timeline(count=50, screen_name=user_screen_name)

	all_tweets = []
	date = datetime.datetime(2022, 6, 1)
	for tweet in tweets:
		tweet_text = tweet.text
		date = tweet.created_at
		tweet_date = date.strftime("%A, %d %b %Y")
		tweet_time = date.strftime("%I:%M %p")
		profile_image_url = tweet.user.profile_image_url
		twitter_obj = Twitter(tweet_text, tweet_date, tweet_time, profile_image_url)
		all_tweets.append(twitter_obj)
	# print(all_tweets)
	return all_tweets
# get_tweets('katrinakaiffb')
# print(get_screen_name('amitabh bachhan'))

