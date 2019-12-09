from django.urls import path

from . import views
from pages.views import home


urlpatterns = [
    path('', views.home, name='home'),
   


]