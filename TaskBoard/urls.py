from django.urls import path
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'TaskBoard', TaskViewSet)

urlpatterns = router.urls