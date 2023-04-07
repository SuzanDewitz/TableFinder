from django.urls import path
from . import views


urlpatterns = [
    # ... other URL patterns ...
    path('', views.home, name='home'),
    path('booking/', views.booking_page, name='booking_page'),
]