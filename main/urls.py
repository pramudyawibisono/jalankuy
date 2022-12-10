from django.urls import path
from .views import show_home, show_login

app_name = 'main'
urlpatterns = [
    # path('', show_home, name='show_home'),
    # path('login', show_login, name='show_login'),
]
