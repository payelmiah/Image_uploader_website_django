
from django.contrib import admin
from django.urls import path
from django.conf import settings # import settings because we need to access MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static # import static to serve media files in development
from imageuploader import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home , name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Compare this snippet from main/urls.py:

#print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) 