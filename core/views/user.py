from core.serializers.user import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import CustomUser
from rest_framework.response import Response
from core.serializers import ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# https://dev.to/ki3ani/implementing-jwt-authentication-and-user-profile-with-django-rest-api-part-3-3dh9

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    # Só o superUser pode registrar um novo User, retirar depois
    permission_classes = (AllowAny,) 
    serializer_class = RegisterSerializer

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)