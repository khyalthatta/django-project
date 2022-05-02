from django.contrib import admin
from django.urls import path, include
from calculator.views import operation_view
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', operation_view, name='calc-page'),
    path('finance/', include('finance.urls')),
    path('blog/', include('blog.urls')),
    path('', home_view),
]
