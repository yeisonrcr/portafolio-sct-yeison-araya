from django.urls import path
from .views.views_home import home, about

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('sobre-mi/', about, name='about'),
]
