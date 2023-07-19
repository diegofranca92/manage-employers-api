
from core.models import Company
from core.serializers import CompanySerializer

from rest_framework.viewsets import ModelViewSet


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer