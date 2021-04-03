from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('Chapters/', views.Chapters, name='Chapters'),
    path('Check_Content/', views.Check_Content, name='Check_Content'),
    path('Page_Title/', views.Page_Title, name='Page_Title'),
]