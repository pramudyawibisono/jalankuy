from django.urls import path
from .views import *

app_name = 'manageData'
urlpatterns = [
    path('admin_home', home_admin, name='home_admin'),
    path('admin_home/view-destination-area', view_destination_area, name='view-destination-area'),
    path('admin_home/add-destination-area', add_destination_area, name='add-destination-area'),
    path('admin_home/view-site', view_site, name='view-site'),
    path('admin_home/add-site', add_site, name='add-site'),
    path('admin_home/view-accommodation', view_accommodation, name='view-accommodation'),
    path('admin_home/add-accommodation', add_accommodation, name='add-accommodation'),
]


