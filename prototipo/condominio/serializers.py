from rest_framework import serializers
from .models import Morador  # Confirme se o seu modelo se chama exatamente 'Morador'

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'