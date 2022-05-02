from django.urls import path

from .views import (
    SimpleAPIView,
    ContactView,
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
    ContactRetrieveView,
    ContactDestroyView,
    ContactModelViewSet,
    ArticleModelViewSet
)

from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('contact-viewset', ContactModelViewSet, basename='contact-viewset')
r.register('article-viewset', ArticleModelViewSet, basename='article-viewset')

urlpatterns = [
    path('contact-create/', ContactCreateView.as_view()),
    path('contact-list/', ContactListView.as_view()),
    path('contact-update/<int:pk>/', ContactUpdateView.as_view()),
    path('contact-retrieve/<int:pk>/', ContactRetrieveView.as_view()),
    path('contact-destroy/<int:pk>/', ContactDestroyView.as_view()),
    path('contact/', ContactView.as_view()),
    path('', SimpleAPIView.as_view())
]

urlpatterns += r.urls
