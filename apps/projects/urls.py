from django.urls import path
from .views.views_project_list import project_list
from .views.views_project_detail import project_detail

app_name = 'projects'

urlpatterns = [
    path('', project_list, name='list'),
    path('<slug:slug>/', project_detail, name='detail'),
]
