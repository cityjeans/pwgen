from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pwgen/", include("pwgen.urls")),
    path('admin/', admin.site.urls),
]
