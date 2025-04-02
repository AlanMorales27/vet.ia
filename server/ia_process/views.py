import json
from django.shortcuts import render
from rest_framework import generics
from ia_process.models import review
from ia_process import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from ia_process.tensor_process import predecir_enfermedad


@csrf_exempt
def into_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('name', '')

        # modified_text = text + ' modified'
        modified_text = predecir_enfermedad(text)

        return JsonResponse({'texto_mod': modified_text})
    

    else: 
        return JsonResponse({'error': 'POST method is required'}, status=405)