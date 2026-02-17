from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm, StudentForm, MarksForm
from .models import Student, Marks, Attendance
from rest_framework import viewsets
from .serializers import StudentSerializer, MarksSerializer, AttendanceSerializer


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()

            login(request, user)
            return redirect('dashboard')

    else:
        user_form = UserRegisterForm()
        student_form = StudentForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'student_form': student_form
    })


def user_login(request):
    form = AuthenticationForm(data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')

    return render(request, 'login.html', {'form': form})




def dashboard(request):
    student = Student.objects.get(user=request.user)
    marks = Marks.objects.filter(student=student)
    attendance = Attendance.objects.filter(student=student)

    return render(request, 'dashboard.html', {
        'student': student,
        'marks': marks,
        'attendance': attendance
    })



def user_logout(request):
    logout(request)
    return redirect('login')
from .forms import MarksForm
from django.contrib.auth.decorators import login_required

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MarksForm()

    return render(request, 'add_marks.html', {'form': form})



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

