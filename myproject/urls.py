from django.contrib import admin
from django.urls import path, include
from concess import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api-root'),
    path('api/', include('concess.urls')),
]