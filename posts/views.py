from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def posts(request):
    post_qs = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'post_qs': post_qs})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', context={'post': post})


def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('posts:post_detaildetail', post_id=new_post.id)
    else:
        post_form = PostForm()
    return render(request, 'posts/post_form.html', {'form': post_form})
