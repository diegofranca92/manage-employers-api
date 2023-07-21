from rest_framework.serializers import ModelSerializer
from core.models import Employer

class EmployerDetailSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        depth = 2

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'