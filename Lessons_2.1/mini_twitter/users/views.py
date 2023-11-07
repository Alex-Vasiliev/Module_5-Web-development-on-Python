from django.shortcuts import render
from .models import Users


def list_users(request):
    users = Users.objects.all()
    return render(request, 'list_users.html', {'users': users})
