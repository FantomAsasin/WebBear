from django.urls import path
from . import views
urlpatterns = [
    path('', views.UPload_content, name='UPload_content'),
    path('CreateChapters/', views.CreateChapters, name='CreateChapters'),
    path('CreateTitle/', views.CreateTitle, name='CreateTitle'),
] 