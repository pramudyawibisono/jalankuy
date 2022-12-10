"""jalankuy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.urls as main
import accommodation.urls as accommodation
import siteapp.urls as siteapp
import authentication.urls as auth
import destination_area.urls as destination_area
import profil.urls as profil
import manageData.urls as manageData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main)),
    path('<int:destareaid>/accommodations/', include(accommodation)),
    path('auth/', include(auth)),
    path('<int:destareaid>/sites/', include(siteapp)),
    path('', include(destination_area)),
    path('profile/', include(profil)),
    path('admin_home/', include(manageData))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
