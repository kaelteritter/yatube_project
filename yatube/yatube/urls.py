# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='urls')),
    path('auth/', include('django.contrib.auth.urls')), 
] 