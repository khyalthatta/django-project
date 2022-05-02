from django.urls import path
from .views import list_view, blog_create

urlpatterns = [
    path('create/', blog_create),
    path('', list_view)
]
