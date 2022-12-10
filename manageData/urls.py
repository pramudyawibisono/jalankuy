from django.urls import path
from .views import *

app_name = 'manageData'
urlpatterns = [
    path('', home_admin, name='home_admin'),
    path('view/<str:idcommand>', view_all_list, name='view-all-list'),
    path('add-destination-area', add_destination_area, name='add-destination-area'),
    path('add-site', add_site, name='add-site'),
    path('add-accommodation', add_accommodation, name='add-accommodation'),
]