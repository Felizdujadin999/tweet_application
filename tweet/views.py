from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from tweet.models import Post


def welcome(request):
    tweets = Post.objects.all()
    return render(request, 'tweet/home.html', {"tweets": tweets})
    # return HttpResponse("Welcome Felix, This is django oh!!!!!")


def tweet_detail(request, pk):
    # tweet = get_object_or_404(Post, pk=pk) // you can use this also if you want to go the django route.
    try:
        tweet = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse("Tweet with the given id does not exist..")
    return render(request, 'tweet/tweet-detail.html', {"tweet": tweet})


class CreateTweet(generic.CreateView):
    model = Post
    template_name = 'tweet/create-tweet.html'
    fields = ['tweet', 'author']  # '__all__'//you can use this to generify it all but it's not a good practice...
