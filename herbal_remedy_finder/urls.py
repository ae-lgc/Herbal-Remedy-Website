from herbs import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from herbs.views import herb_list, herb_detail, home  
from django.conf import settings
from django.conf.urls.static import static
from herbs.views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  

    # App routes
    path('herbs/', include('herbs.urls')),  # handles /herbs/ and /herbs/herb/<pk>/
    path('api/', include('herbs.api_urls')),   
]

    

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
