from django.urls import path
from .views import *

app_name = 'accommodation'
urlpatterns = [
    path('destination-area/<int:destareaid>/accommodations', 
        accommodations, name='accommodation_list'),
    path('destination-area/<int:destareaid>/accommodations/<int:accommid>', 
        accommodation_detail, name='accommodation_detail'),
    path('destination-area/<int:destareaid>/accommodations/<int:accommid>/add-review', 
        add_accommodation_review, name='add_accommodation_review'),
]
