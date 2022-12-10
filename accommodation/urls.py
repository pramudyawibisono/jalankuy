from django.urls import path
from .views import *

app_name = 'accommodation'
urlpatterns = [
    path('', accommodations, name='accommodation_list'),
    path('<int:accommid>', accommodation_detail, name='accommodation_detail'),
    path('<int:accommid>/add-review', add_accommodation_review, name='add_accommodation_review'),
]
