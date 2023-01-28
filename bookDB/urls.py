from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read/', include('booklistapp.api.urls')),
    path('publisher/', include('booklistapp.api.urls')),
]
