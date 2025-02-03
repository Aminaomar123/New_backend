from django.urls import path
from .views import *


urlpatterns = [
    path('customer/', manage_customer, name='customer-list'),
    path('customer/<int:pk>/', manage_customer, name='customer-detail'),

    # Add other views similarly
    path('equipment/', manage_equipment, name='equipment-list'),
    path('equipment/<int:pk>/', manage_equipment, name='equipment-detail'),

    path('booking/', manage_booking, name='booking-list'),
    path('booking/<int:pk>/', manage_booking, name='booking-detail'),

    path('payment/', manage_payment, name='payment-list'),
    path('payment/<int:pk>/',manage_payment, name='payment-detail'),
]
