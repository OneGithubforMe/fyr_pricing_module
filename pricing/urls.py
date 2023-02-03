from django.urls import path
from .views import CalculatePricing

urlpatterns = [
    path('calculate', CalculatePricing.as_view() , name="calculate_pricing"),
]
