from django.urls import path
from .views import (home_view, tweet_detail_view, 
	tweet_list_view, tweet_create_view,
	tweet_delete_view, tweet_action_view)
	

urlpatterns = [
	path('', home_view , name='home'),
	path('tweets/<int:tweet_id>/', tweet_detail_view, name='detail'),
	path('tweets/', tweet_list_view, name='list'),
	path('tweets-create', tweet_create_view, name='create'),
	path('api/tweets/action/', tweet_action_view),
	path('api/tweets/<int:tweet_id>/delete/',tweet_delete_view, name='delete')
]