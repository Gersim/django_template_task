from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('company-profile/<str:pk>', views.open_company_profile, name='company-profile'),
]
