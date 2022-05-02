from django.urls import path

from .views import contact_view, home_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('contact-view/', contact_view, name='contact-view'),
    path('login/', obtain_auth_token, name='login'),
    path('', home_view, name='home')
]
