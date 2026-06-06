from django.urls import path
from .views.views_contact import contact, contact_success

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contact'),
    path('gracias/', contact_success, name='success'),
]
