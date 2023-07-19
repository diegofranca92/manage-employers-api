from rest_framework.serializers import ModelSerializer

from core.models import Company, Employer

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        depth = 2