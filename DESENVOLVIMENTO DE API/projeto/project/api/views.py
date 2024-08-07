import requests
from django.shortcuts import render
from rest_framework import generics, filters
from app.models import Clients
from .serializers import ClientsApiSerializer
from .permissions import IsOwnerOrReadOnly
import pprint
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def protected_view(request):
    return Response({"message": "This is a protected view"})


class ClientsListCreate(generics.ListCreateAPIView):  
    queryset = Clients.objects.all()
    serializer_class = ClientsApiSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'cpf_cnpj', 'rg_ie', 'state']
    ordering_fields = ['created_at']

class ClientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsApiSerializer
    permission_classes = [IsOwnerOrReadOnly]

def show_curl_command(request):
    return render(request, 'api/show_curl_command.html')

def get_token_view(request):
    # Dados para a requisição
    payload = {
        'username': 'admin',
        'password': 'admin'
    }

    # URL da API para obter o token
    url = 'http://127.0.0.1:8000/api/token/'

    # Fazer a requisição POST
    response = requests.post(url, json=payload)
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obter o token da resposta
        token_data = response.json()
        access_token = token_data.get('access')
        refresh_token = token_data.get('refresh')
    else:
        access_token = None
        refresh_token = None

    # Renderizar o template com os tokens
    return render(request, 'api/show_tokens.html', {
        'access_token': access_token,
        'refresh_token': refresh_token
    })