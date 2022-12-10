from django.urls import path
from .views import *

app_name = 'siteapp'
urlpatterns = [
    path('', sites, name='site_list'),
    path('<int:siteid>', site_detail, name='site_detail'),
    path('<int:siteid>/add-review', add_site_review, name='site_review'),
]