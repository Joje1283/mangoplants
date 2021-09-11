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
            return redirect('posts:post_detail', pk=new_post.id)
    else:
        post_form = PostForm()
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        # request.POST: 수정할 내용, instance인자: 수정 대상 지정
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_detail', pk=post.id)
    else:
        post_form = PostForm(instance=post)  # post데이터가 form에 바운드된 상태로 데이터가 생성된다.
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:posts')
    else:
        return render(request, 'posts/post_confirm_delete.html')
