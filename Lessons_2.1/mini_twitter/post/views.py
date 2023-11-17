from django.shortcuts import render
from .models import Post, Comment
from users.models import Users


def list_post(request, username=None):
    if username:
        user = Users.objects.get(username=username)
        post = Post.objects.filter(users=user)
    else:
        post = Post.objects.all()

    context = {'post': post, 'username': user}
    return render(request, 'post/post_list.html', context)


def list_comments(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'post/comments_list.html', context)
