from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('booklistapp.api.urls')),
    path('publishers/', include('booklistapp.api.urls')),
]
