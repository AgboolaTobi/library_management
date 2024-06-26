"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import djoser
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import urls
from django.urls import path, include
from django.conf import settings

admin.site.site_header = 'Librarian Panel'
admin.site.index_title = 'Librarian administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('auth/', include(urls)),
    path('demo/', include('demo.urls')),
    path('catalog/', include('catalog.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
