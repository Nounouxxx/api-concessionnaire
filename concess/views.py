from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view



from .models import Concessionnaire, Vehicule
from .serializers import ConcessionnaireSerializer, VehiculeSerializer


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny


@api_view(['GET'])
def api_root(request):
    """
    Racine de l'API qui liste les endpoints principaux.
    """
    return Response({
        "concessionnaires": "/api/concessionnaires/",
        "users": "/api/users/",
        "token": "/api/token/",
        "refresh_token": "/api/refresh_token/"
    })

class ConcessionnaireList(APIView):
    permission_classes = [AllowAny]


def get(self, request):
    qs = Concessionnaire.objects.all()
    serializer = ConcessionnaireSerializer(qs, many=True)
    return Response(serializer.data)




class ConcessionnaireDetail(APIView):
    permission_classes = [AllowAny]


def get(self, request, pk):
    obj = get_object_or_404(Concessionnaire, pk=pk)
    serializer = ConcessionnaireSerializer(obj)
    return Response(serializer.data)




class VehiculeListByConcessionnaire(APIView):
    permission_classes = [AllowAny]


def get(self, request, concessionnaire_pk):
    concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
    qs = concessionnaire.vehicules.all()
    serializer = VehiculeSerializer(qs, many=True)
    return Response(serializer.data)



class VehiculeDetail(APIView):
    permission_classes = [AllowAny]


def get(self, request, concessionnaire_pk, vehicule_pk):
    concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
    vehicule = get_object_or_404(Vehicule, pk=vehicule_pk, concessionnaire=concessionnaire)
    serializer = VehiculeSerializer(vehicule)
        
    return Response(serializer.data)




# Bonus: création d'utilisateur (POST /api/users/)
class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'detail': 'username and password required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'detail': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)

