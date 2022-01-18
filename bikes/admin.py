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

@admin.register(Spare)
class SpareAdmin(admin.ModelAdmin):
    list_display = ["name", "buying_price", "resell_price", "current_stock", "restock_level"]    


@admin.register(SpareSale)
class SpareSaleAdmin(admin.ModelAdmin):
    list_display = ["spare", "quantity", "total_price", "date_sold", "sold_by"]


@admin.register(RentBike)
class RentBikeAdmin(admin.ModelAdmin):
    list_display = ["bike", "renter_name", "rent_period", "returned_condition", "total_charge"]



