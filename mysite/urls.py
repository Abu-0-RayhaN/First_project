
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('conatct/',include('contact.urls')),
    path('authentication/',include('authentication.urls')),
    path('portfolio/',include('portfolio.urls')),
    

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
