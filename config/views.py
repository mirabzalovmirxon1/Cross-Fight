from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')  # agar index.html templates ichida bo'lsa

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard.html')

            elif user.role == 'trainer':
                return redirect('trainer_dashboard.html')

            elif user.role == 'student':
                return redirect('dashboard.html')

    return render(request, 'login.html')


@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('/')
    return render(request, 'admin_dashboard.html')


@login_required
def trainer_dashboard(request):
    if request.user.role != 'trainer':
        return redirect('/')
    return render(request, 'trainer_dashboard.html')


@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return redirect('/')
    return render(request, 'student_dashboard.html')