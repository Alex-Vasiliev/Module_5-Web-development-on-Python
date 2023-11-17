from django.shortcuts import render
from .models import Users


def list_users(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'users/user_list.html', context)
