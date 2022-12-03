from django.urls import path
from .views import *

app_name = 'manageData'
urlpatterns = [
    path('admin_home', home_admin, name='home_admin'),
    path('admin_home/view/<str:idcommand>', view_all_list, name='view-all-list'),
    path('admin_home/add-destination-area', add_destination_area, name='add-destination-area'),
    path('admin_home/add-site', add_site, name='add-site'),
    path('admin_home/add-accommodation', add_accommodation, name='add-accommodation'),
]


