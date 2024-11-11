# client/models.py
from django.contrib.auth.models import User
from django.db import models

#model revolves around administator access. stores users details and permissions
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permissions = models.TextField(help_text="Permissions for this admin user")
    
    def __str__(self):
        return f"{self.user.username} - Admin"

# client/models.py to store additional details of students
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - Student"
