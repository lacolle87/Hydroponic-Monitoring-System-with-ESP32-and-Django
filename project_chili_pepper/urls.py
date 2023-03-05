from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('hydro.urls')),
    path('admin/', admin.site.urls),
]
