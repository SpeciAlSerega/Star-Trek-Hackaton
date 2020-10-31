from django.contrib import admin
from django.urls import include, path

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='about'),
    path('/contacts', contacts, name='contacts'),
    path('/service', service, name='service'),
    path('/add', add, name='add'),
    path('/news_portal', news_portal, name='news_portal'),
    path('/card', card, name='card'),
    


# ####################################################################################
    path('help/', help, name='help'),
    path('cabinet/', cabinet, name='cabinet'),
# ####################################################################################
    path('posts/', posts_list, name='posts_list_url'),
    path('tags/', tags_list, name='tags_list_url'),
# ####################################################################################
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tag/create/', TagCreate.as_view(), name = 'tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
# ####################################################################################
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update'),
# ####################################################################################
    # path('post/<str:slug>/delete/', TagDelete.as_view(), name='post_delete_url'),  
    # path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),  









]