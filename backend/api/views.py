from django.shortcuts import render

# backend/api/views.py
from django.http import JsonResponse

def hello_api(request):
    return JsonResponse({'message': 'Hello from Django backend!'})
