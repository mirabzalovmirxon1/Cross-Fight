# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, AssignmentViewSet, SubmissionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]