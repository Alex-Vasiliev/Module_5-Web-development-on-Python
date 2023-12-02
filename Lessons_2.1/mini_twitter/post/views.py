from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from users.models import Users


def list_post(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'post/post_list.html', context)


def list_postf(request, username=None):
    if username:
        user = get_object_or_404(Users, username=username)
        post = Post.objects.filter(users=user)
    else:
        post = Post.objects.all()

    context = {'post': post, 'username': username}
    return render(request, 'post/post_list.html', context)


def list_comments(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'post/comments_list.html', context)
