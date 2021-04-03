from django.contrib import admin
from django.urls import path

from IMGcontroll import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.image_upload_view),
    path('check/', views.image_check),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)