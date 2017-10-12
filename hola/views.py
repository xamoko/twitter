from django.shortcuts import render
from django.http import HttpResponse
from twython import Twython

# Create your views here.
def index(request):
	APP_KEY = '08tuNF9XKEP7b5Z0QHyGe1SZU'
	APP_SECRET = 'mxPlt1YAQeRkYRnvCiB1RWSw49hZ2ixAsdJoid5FkDNQxlguoO'
	screen_name = "xamoko"
	twitter = Twython( APP_KEY, APP_SECRET, oauth_version=2 )
	followers = twitter.get_followers_ids(screen_name = screen_name)
	tweets = twitter.get_home_timeline()
	return HttpResponse()