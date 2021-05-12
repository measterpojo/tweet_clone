from django.contrib import admin

from .models import Tweet, TweetLikes

class TweeTLikeAdmin(admin.TabularInline):
	model  = TweetLikes


class TweetAdmin(admin.ModelAdmin):
	inlines = [TweeTLikeAdmin]
	list_display = ['__str__', 'user']
	search_fields = ['user_username', 'user_email', 'content']
	class Meta:
		model = Tweet

admin.site.register(Tweet, TweetAdmin)