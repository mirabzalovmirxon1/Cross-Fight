from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API SCHEMA
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # SWAGGER
    path('api/', SpectacularSwaggerView.as_view(url_name='schema')),

    # APPLAR
    path('api/', include('account.urls')),
    path('api/', include('training.urls')),
]