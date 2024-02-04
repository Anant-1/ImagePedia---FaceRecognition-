import requests
import tweepy
from datetime import datetime
from googlesearch import search
from dotenv import load_dotenv
import os
load_dotenv()

class Twitter:
	def __init__(self, tweet, tweet_date, tweet_time, tweet_image_url):
		self.tweet = str(tweet)
		self.tweet_date = str(tweet_date)
		self.tweet_time = str(tweet_time)
		self.tweet_image_url = str(tweet_image_url)

	def __repr__(self):
		return f'{self.tweet} -- {self.tweet_date} -- {self.tweet_image_url}'

url = "https://twitter-api45.p.rapidapi.com/timeline.php"
headers = {
	"X-RapidAPI-Key": os.environ['API_KEY'],
	"X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
}

def get_screen_name(face_name):
	# to search
	query = face_name.lower() + " twitter screen name"
	res = search(query, tld="co.in", num=5, stop=5, pause=2)
	link = ''
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
	print(screen_name)
	return screen_name

def get_tweets(face_name):
	try:
		all_tweets = []
		screen_name = get_screen_name(face_name)
		querystring = {"screenname":screen_name}
		response = requests.get(url, headers=headers, params=querystring).json()
		if 'timeline' in response and len(response['timeline']) > 0:
			tweets = response['timeline']
			avatar = 'https://twirpz.files.wordpress.com/2015/06/twitter-avi-gender-balanced-figure.png'
			for tweet in tweets:
				tweet_image_url = ''
				description = 'A User'

				tweet_text = tweet['text']
				# print('--', tweet_text)
				date_str = str(tweet['created_at'])
				date = datetime.strptime(date_str, '%a %b %d %H:%M:%S %z %Y')
				tweet_date = date.strftime("%A, %d %b %Y")
				tweet_time = date.strftime("%I:%M %p")

				if 'media' in tweet and tweet['media'] is not None and 'photo' in tweet['media'] and len(tweet['media']['photo']) > 0 and 'media_url_https' in tweet['media']['photo'][0] and tweet['media']['photo'][0]['media_url_https'] is not None:
					tweet_image_url = tweet['media']['photo'][0]['media_url_https']
				
				elif "retweeted_tweet" in tweet and tweet['retweeted_tweet'] is not None and 'media' in tweet['retweeted_tweet'] and tweet['retweeted_tweet']['media'] is not None and 'photo' in tweet['retweeted_tweet']['media'] and len(tweet['retweeted_tweet']['media']['photo']) > 0 and 'media_url_https' in tweet['retweeted_tweet']['media']['photo'][0] and tweet['retweeted_tweet']['media']['photo'][0]['media_url_https'] is not None:
					tweet_image_url = tweet['retweeted_tweet']['media']['photo'][0]['media_url_https']

				twitter_obj = Twitter(tweet_text, tweet_date, tweet_time, tweet_image_url)

				all_tweets.append(twitter_obj)

			if 'user' in response and response is not None and 'avatar' in response['user'] and response['user']['avatar'] is not None and 'desc' in response['user'] and response['user']['desc'] is not None:
				avatar = response['user']['avatar']
				description = response['user']['desc']
				print(avatar, description)

			# print(all_tweets)
			return all_tweets, avatar, description
		else:
			raise Exception("No Tweets Found!")
	except Exception as  e:
		print('Error occured in finding tweets ', e)
		return [],'',''
# get_screen_name('nirmala sitaraman')
get_tweets('nirmala sitaraman')
