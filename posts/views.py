from django.shortcuts import render
from .models import Post


def posts(request):
    post_qs = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'post_qs': post_qs})
