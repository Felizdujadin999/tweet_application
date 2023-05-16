from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome, name='home'),
    path("tweet_detail/<int:pk>/", views.tweet_detail, name='tweet-detail'),
    path("create-tweet/", views.CreateTweet.as_view(), name='create-tweet')
]
