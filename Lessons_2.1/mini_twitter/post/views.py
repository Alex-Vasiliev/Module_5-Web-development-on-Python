from django.shortcuts import render
from .models import Post, Comment


def list_post(request):
    post = Post.objects.all()
    return render(request, 'list_post.html', post)


def list_comments(request):
    comments = Comment.objects.all()
    return render(request, 'list_comment.html', comments)
