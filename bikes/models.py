from enum import auto
from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def employee_address(self):
        return self.address + "-"+self.city+" , "+self.country


BIKE_CONDITIONS = (
    ("Good", "Good"),
    ("Bad", "Bad"),
)

AVAILABILITY_CHOICES = (
    ("1", "Available"),
    ("2", "Not Available"),
)

class Bike(models.Model):
    bike_number = models.CharField(max_length=200, unique=True, primary_key=True)
    condition = models.CharField(max_length=200, choices=BIKE_CONDITIONS)
    price = models.FloatField(default=0)
    rental_rate = models.FloatField(default=0)
    availability = models.CharField(max_length=200, default="1", choices=AVAILABILITY_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    added_by =models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.bike_number

    def get_absolute_url(self):
        return reverse("home")


RENTAL_PERIODS = (
    (1, "1 Hour"),
    (2, "2 Hours"),
    (3, "3 Hours"),
    (4, "4 Hours"),
    (5, "5 Hours"),
    (6, "6 Hours"),
    (7, "7 Hours"),
    (8, "8 Hours"),
    (9, "9 Hours"),
    (10, "10 Hours"),
    (11, "11 Hours"),
    (12, "12 Hours"),

)    


class Rental(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    renter_id = models.CharField(max_length=200)
    rental_period = models.IntegerField(choices=RENTAL_PERIODS)
    returned_condition = models.CharField(max_length=200, choices=BIKE_CONDITIONS)
    damage_fee = models.FloatField(default=0)
    overtime_fee = models.FloatField(default=0)
    total_charged = models.FloatField(default=0)
    time_left = models.DateTimeField(auto_now_add=True)
    time_returned = models.DateTimeField(auto_now=True)
    recorded_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.renter_id

    @property
    def rental_fee(self):
        return self.rental_period * self.bike.rental_rate

    @property
    def extra_fee(self):
        return self.damage_fee + self.overtime_fee

    @property
    def total_fee(self):
        return self.rental_fee + self.extra_fee

    def get_absolute_url(self):
        return reverse("rentals")
    