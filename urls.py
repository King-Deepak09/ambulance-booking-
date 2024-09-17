# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_ambulance, name='book_ambulance'),
    path('bookings/', views.list_bookings, name='list_bookings'),
]
