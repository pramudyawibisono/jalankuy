from django.urls import path, include
from .views import index, edit_profile, edit_password, lupa_password
urlpatterns = [
    path('', index, name="index"),
    path('edit/', edit_profile, name="edit_profile"),
    path('password/edit', edit_password, name="edit_password"),
    path('password/lupa', lupa_password, name="lupa_password"),
    
]
