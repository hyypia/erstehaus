from django.http import Http404
from django.shortcuts import render

from .models import Post


def news_index(request):
    try:
        news = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("News not found")
    return render(request, "news/news.html", {"news": news})


def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post not found")

    return render(request, "news/post_detail.html", {"post": post})
