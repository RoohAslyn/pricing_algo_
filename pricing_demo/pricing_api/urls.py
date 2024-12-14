from django.urls import path
from .views import adjust_prices

urlpatterns = [
    path('adjust-prices/', adjust_prices, name='adjust_prices'),
]
