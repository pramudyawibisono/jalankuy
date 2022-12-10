from django.urls import path
from .views import *

app_name = 'destination_area'
urlpatterns = [
    path('', destinations, name='destination-area'),
    path('<int:id>', destination_detail, name="destination-area-detail"),
    path('<int:id>/add-review', add_destination_area_review, name="add-destination-area-review")
]