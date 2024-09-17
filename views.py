# views.py
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

def book_ambulance(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bookings')  # Redirect to list of bookings after saving
    else:
        form = BookingForm()
    return render(request, 'book_ambulance.html', {'form': form})

def list_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'list_bookings.html', {'bookings': bookings})
