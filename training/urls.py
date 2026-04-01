from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('', include(router.urls)),
]