from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import HomeView
from .views import (
    login_view,
    admin_dashboard,
    trainer_dashboard,
    student_dashboard
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # API SCHEMA
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # SWAGGER
    path('api/', SpectacularSwaggerView.as_view(url_name='schema')),

    path('', HomeView.as_view()),  # frontend

]

urlpatterns += [
    path('', login_view, name='login'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('trainer-dashboard/', trainer_dashboard, name='trainer_dashboard'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
]