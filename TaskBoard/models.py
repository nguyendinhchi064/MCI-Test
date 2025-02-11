from django.db import models
from Employee.models import Employee
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')])
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
