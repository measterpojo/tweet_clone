
from django.contrib import admin
from django.urls import path, include

from tweets.views import tweet_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweets.urls')),
    path('api/tweets', tweet_list_view),
]
