from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()

router.register(r'company', CompanyViewSet, basename='company')
router.register(r'employee', EmployeeViewSet, basename='employee')

urlpatterns = router.urls