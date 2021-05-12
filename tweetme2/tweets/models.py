from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL



class TweetLikes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
	parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
	content = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, blank=True, related_name='tweet_users', through=TweetLikes)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-id']

	@property
	def is_retweet(self):
		return self.parent != None