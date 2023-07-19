
from django.contrib import admin
from django.urls import path, include

from core import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'employer', views.EmployerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
