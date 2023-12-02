from django.urls import path
from . import views

urlpatterns = [

    path('', views.list_post, name='list_post'),
    path('post/<str:username>/', views.list_postf, name='post_list_filtered'),
    path('comment/', views.list_comments, name='list_comment')
]
