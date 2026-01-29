"""
URL configuration for pract project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('myapp.urls')),
    # path('',include('myapp1.urls')),
    # path('',include('myapp2.urls')),
    # path('',include('myapp3.urls')),
    # path('',include('myapp4.urls')),
    # path('',include('myapp5.urls')),
    # path('',include('myapp6.urls')),
    # path('',include('myapp7.urls')),
    # path('',include('myapp8.urls')),
    # path('',include('myapp9.urls')),
    # path('',include('api1.urls')),
    # path('',include('api2.urls')),
    # path('',include('api3.urls')),
    # path('',include('api4.urls')),
    path('',include('api5.urls')),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh_pair'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()