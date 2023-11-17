from django.urls import path
from . import views

urlpatterns = [

    path('', views.list_post, name='list_post'),
    path('<str:username>/', views.list_post, name='post_list_filtered'),
    path('comment/', views.list_comments, name='list_comment')
]
