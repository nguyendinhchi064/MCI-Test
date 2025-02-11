from django.urls import path
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls