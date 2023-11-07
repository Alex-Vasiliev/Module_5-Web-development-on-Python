from django.urls import path
from . import views

urlpatterns = [

    path('post/', views.list_post, name='list_post'),
    path('comment', views.list_post, name='list_comment')
]
