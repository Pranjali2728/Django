from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm


# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(
                request,
                'students/login.html',
                {'error': 'Invalid Username or Password'}
            )

    return render(request, 'students/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard
@login_required
def dashboard(request):
    total_students = Student.objects.count()

    return render(
        request,
        'students/dashboard.html',
        {'total_students': total_students}
    )


# Student List
@login_required
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )


# Add Student
@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )


# Update Student
@login_required
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )


# Delete Student
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'students/delete_confirm.html',
        {'student': student}
    )