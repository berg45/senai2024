from rest_framework import serializers
from app.models import Clients

class ClientsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = [ 'id', 'name', 'cpf_cnpj', 'rg_ie', 'zip_code', 'address', 'neighborhood', 'number', 'city', 'state', 'updated_at', 'deleted_at']
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("O título deve ter pelo menos 5 caracteres.")
        return value
