from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Tweet

from rest_framework.test import APIClient

User = get_user_model()


class TweetTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='player1', password='somepassword')
		Tweet.objects.create(content='heyya', user=self.user)

	def test_tweet_create(self):
		tweet = Tweet.objects.create(content='2nd_heyya', user=self.user)
		self.assertEqual(tweet.id, 2)
		self.assertEqual(tweet.user, self.user)


	def get_client(self):	
		client = APIClient()
		client.login(username=self.user.username, password='somepassword')
		return client

	def test_tweet_list(self):
		client = self.get_client()
		response = client.get('/tweets/')
		self.assertEqual(response.status_code, 200)
		print(response)

	def test_action_like(self):
		client = self.get_client()
		response = client.post("/api/tweets/action/", {"id":1, "action": 'like'})
		self.assertEqual(response.status_code, 200)
		response = client.post("/api/tweets/action/", {"id":1, "action": 'unlike'})
		self.assertEqual(response.status_code, 200)
		like_count = response.json().get('likes')
		self.assertEqual(like_count, 0)

	def test_action_retweet(self):
		client = self.get_client()
		response = client.post("/api/tweets/action/", {"id":1, "action": 'retweet'})
		self.assertEqual(response.status_code, 201)

	def test_tweet_create_api_view(self):
		request_data = {'content':'was g'}
		client = self.get_client()
		response = client.post("/tweets-create", request_data)
		self.assertEqual(response.status_code, 201)
