from django.contrib import admin
from django.urls import path, re_path, include

api_urlpatterns = [
    path("tasks/", include("tasks.urls")),
]

urlpatterns = [
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path("api/v1/", include(api_urlpatterns)),
]
