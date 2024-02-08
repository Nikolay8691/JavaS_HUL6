from django.urls import path
from . import views

app_name = 'scroll'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('buttonhide', views.index_hide, name = 'index_hide'),
    path('posts', views.posts, name = 'posts'),
]
