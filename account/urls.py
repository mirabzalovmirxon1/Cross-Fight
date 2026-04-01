from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_student, MyTokenObtainPairView

# router = DefaultRouter()
# router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    # path('', include(router.urls)),

    # 🔑 AUTH
    path('register/', register_student, name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token'),
]