from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_student, TokenObtainPairView

# router = DefaultRouter()
# router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    # path('', include(router.urls)),

    # 🔑 AUTH
    path('register/', register_student, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token'),
]