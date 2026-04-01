from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import AccountViewSet
from training.views import LessonViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]