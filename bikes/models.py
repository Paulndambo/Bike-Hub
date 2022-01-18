from enum import auto
from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User

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

class Bike(models.Model):
    bike_number = models.CharField(max_length=200, unique=True, primary_key=True)
    condition = models.CharField(max_length=200, choices=BIKE_CONDITIONS)
    price = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    added_by =models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.bike_number


class Spare(models.Model):
    name = models.CharField(max_length=200)
    buying_price = models.IntegerField(default=0)
    resell_price = models.IntegerField(default=0)
    current_stock = models.IntegerField(default=0)
    restock_level = models.IntegerField(default=0)
    date_acquired = models.DateField(auto_now_add=True)
    date_restocked = models.DateField(auto_now=True)
    recorded_by = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class SpareSale(models.Model):
    spare = models.ForeignKey(Spare, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    date_sold = models.DateField(auto_now_add=True)
    sold_by = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.spare.name

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


class RentBike(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    renter_id = models.CharField(max_length=200)
    renter_name = models.CharField(max_length=200)
    rent_period = models.IntegerField(choices=RENTAL_PERIODS)
    bike_rent_rate = models.IntegerField(default=0)
    time_left = models.DateTimeField(auto_now_add=True)
    time_returned = models.DateTimeField(auto_now=True)
    returned_condition = models.CharField(max_length=200, choices=BIKE_CONDITIONS)
    total_charge = models.FloatField(default=0)
    recorded_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.renter_name
    