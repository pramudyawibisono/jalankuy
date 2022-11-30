from django.urls import path
from .views import home_admin

app_name = 'manageData'
urlpatterns = [
    path('admin_home', home_admin, name='home_admin'),
]


