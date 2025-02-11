from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework import filters

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'assigned_to__name']