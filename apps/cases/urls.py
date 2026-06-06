from django.urls import path
from .views.views_case_list import case_list
from .views.views_case_detail import case_detail

app_name = 'cases'

urlpatterns = [
    path('', case_list, name='list'),
    path('<slug:slug>/', case_detail, name='detail'),
]
