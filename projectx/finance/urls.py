from django.urls import path

from .views import annuity_view, compound_view, amortized_view

urlpatterns = [
    path('annuity/', annuity_view),
    path('compound/', compound_view),
    path('amortized/', amortized_view),
]
