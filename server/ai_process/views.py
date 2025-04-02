from rest_framework.decorators import api_view;
from rest_framework.response import Response;
from rest_framework import status;
from django.shortcuts import render;
from django.http import HttpResponse;
from . import serializers;
from . import tensor_process;

# Create your views here.
@api_view(['POST'])
def anamnesis_request(request):
    serializer = serializers.AnamnesisSerializer(data = request.data);
    if serializer.is_valid():
        responseData = serializer.save();
        vaccination = "vacunas al dia" if responseData.vaccination else "sin vacunas al dia";
        prompt = f"Perro de {responseData.age} años de edad, {vaccination}. el propietario observa: {responseData.observation}";
        tensor_response =tensor_process.predecir_enfermedad(prompt);
        print(tensor_response);
        return Response({
            "data": serializer.data,
            "tensor_response": tensor_response
        }, status=status.HTTP_201_CREATED);
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST);
    
