from django.db import models
from users.models import Users


class Post(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.users} Post: {self.title}'


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post: {self.post}'
