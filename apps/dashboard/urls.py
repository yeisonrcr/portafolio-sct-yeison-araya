from django.urls import path
from django.contrib.auth import views as auth_views
from .views.views_dashboard import dashboard_home

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
