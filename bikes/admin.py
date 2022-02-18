from django.contrib import admin
from . models import *
# Register your models here.
admin.site.site_header = "BIKE HUB"
admin.site.site_title = "BIKE HUB"

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "id_number", "phone_number", "employee_address"]

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ["bike_number", "condition", "price"]


@admin.register(Rental)
class RentBikeAdmin(admin.ModelAdmin):
    list_display = ["bike", "rental_period", "returned_condition", "total_charged"]



