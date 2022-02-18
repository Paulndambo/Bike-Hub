from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Bike, Rental
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
# Create your views here.
@login_required(login_url="login")
def home(request):
    bikes = Bike.objects.all()
    context = {
        "bikes": bikes
    }
    return render(request, "home.html", context)

class NewBike(CreateView):
    model = Bike 
    fields = "__all__"
    template_name = "bikes/new-bike.html"

class UpdateBike(UpdateView):
    model = Bike
    fields = "__all__"
    template_name = "bikes/update-bike.html"

def rentals(request):
    rentals = Rental.objects.all()
    context = {
        "rentals": rentals
    }

    return render(request, "bikes/rentals.html", context)

class RentBike(CreateView):
    model = Rental
    fields = ["bike", "renter_id", "rental_period", "recorded_by"]
    template_name = "bikes/rent-bike.html"

class UpdateRental(UpdateView):
    model = Rental
    fields = ["bike", "returned_condition", "damage_fee", "overtime_fee"]
    template_name = "bikes/update-rental.html"