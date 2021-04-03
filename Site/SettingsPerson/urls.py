from django.urls import path
from . import views
urlpatterns = [
    path('', views.Settings, name='Settings'),
    path('Registr/', views.Registr, name='Registr'),
    path('Auto/', views.Auto, name='Auto'),
] 