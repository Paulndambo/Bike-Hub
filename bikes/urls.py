from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-bike/", views.NewBike.as_view(), name="new-bike"),
    path("update-bike/<str:pk>/", views.UpdateBike.as_view(), name="update-bike"),
    path("rentals/", views.rentals, name="rentals"),
    path("rent-bike/", views.RentBike.as_view(), name="rent-bike"),
    path("update-rental/<str:pk>/", views.UpdateRental.as_view(), name="update-rental"),
]
