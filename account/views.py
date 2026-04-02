from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema



# from .models import Account
from .serializers import AccountSerializer, RegisterSerializer, LoginSerializer


# class AccountViewSet(viewsets.ModelViewSet):
#     queryset = Account.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     # def get_serializer_class(self):
#     #     if self.action == 'create':
#     #         return AccountCreateSerializer
#     #     return AccountSerializer

#     def get_queryset(self):
#         user = self.request.user

#         if user.is_superuser:
#             return Account.objects.all()

#         return Account.objects.filter(id=user.id)

#     def create(self, request, *args, **kwargs):
#         if request.data.get('role') == 'Teacher' and not request.user.is_superuser:
#             return Response(
#                 {"detail": "Faqat admin Teacher qo‘sha oladi"},
#                 status=status.HTTP_403_FORBIDDEN
#             )

#         return super().create(request, *args, **kwargs)


# 🔑 REGISTER (Student)
@extend_schema(
    request=RegisterSerializer,
    responses=AccountSerializer,
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_student(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": AccountSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 🔑 LOGIN (JWT)
@extend_schema(
    request=LoginSerializer,
    responses={200: AccountSerializer},
    description="Student login: email va parol bilan kirish"
)
class StudentLoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": AccountSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # 🔥 ROLE BO'YICHA YO'NALTIRISH
            if user.role == 'admin':
                return redirect('admin_dashboard')

            elif user.role == 'trainer':
                return redirect('trainer_dashboard')

            elif user.role == 'student':
                return redirect('student_dashboard')

            else:
                return redirect('/')
            
    return render(request, 'login.html')