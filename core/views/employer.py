
from core.models import Employer
from core.serializers import EmployerSerializer, EmployerDetailSerializer

from rest_framework.viewsets import ModelViewSet


class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return EmployerDetailSerializer
        if self.action == 'retrieve':
            return EmployerDetailSerializer
        return EmployerSerializer