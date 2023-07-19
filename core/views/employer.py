
from core.models import Employer
from core.serializers import EmployerSerializer

from rest_framework.viewsets import ModelViewSet


class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer