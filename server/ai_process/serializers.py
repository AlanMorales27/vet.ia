from rest_framework import serializers
from .models import anamnesis

class AnamnesisSerializer(serializers.ModelSerializer):
    class Meta: 
        model = anamnesis
        fields = '__all__'