from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Post


def news_index(request):
    news = get_list_or_404(Post)
    return render(request, "news/news.html", {"news": news})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "news/post_detail.html", {"post": post})
