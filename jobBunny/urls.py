from django.contrib import admin
from django.urls import path , include
from auth_app.views import*
from AllViews.views import*

from django.conf.urls.static import static , settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('auth_app.urls')),
    

]+static(settings.STATIC_URL ,document_root=settings.STATIC_ROOT ) + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT )
