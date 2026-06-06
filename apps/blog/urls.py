from django.urls import path
from .views.views_blog_list import blog_list
from .views.views_blog_detail import blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='list'),
    path('<slug:slug>/', blog_detail, name='detail'),
]
