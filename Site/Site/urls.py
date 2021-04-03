from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CheckTitle/', include('CheckTitle.urls')),
    path('CreateTitle/', include('CreateTitle.urls')),
    path('SettingsPerson/', include('SettingsPerson.urls')),
]
