"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from rest_framework.authtoken import views as token_views





urlpatterns = [
    url(r'^$', home_views.index),
    url(r'^home/', include('home.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^admin/', admin.site.urls),
    path('',include("django.contrib.auth.urls")),
    path('api-token-auth/', token_views.obtain_auth_token, name="api-token-auth"),
]
"""
from home import views as home_views
from register import views as register_views
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path(r'', home_views.AddImageView, name="add-image"),
    path('list_images/<int:pk>', home_views.ImageDetailView.as_view(), name='list-images'),
    path(r'admin/', admin.site.urls),
    path(r'home/', include("home.urls")),
    path("members/", include("members.urls")),
    path('members/',include("django.contrib.auth.urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
