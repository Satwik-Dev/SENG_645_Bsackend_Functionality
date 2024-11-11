#client/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    return render(request, 'client/index.html')

# Check if user is in the admin group
def is_admin(user):
    return user.groups.filter(name='admin').exists()

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'client/admin_dashboard.html')

# client/views.py
def is_student(user):
    return user.groups.filter(name='student').exists()

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'client/student_dashboard.html')
