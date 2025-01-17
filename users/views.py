from django.shortcuts import render
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def registration(request):
    if request.method != "POST":
        return JsonResponse({"error":'invalid method'},status=400)
    try:
        data = json.loads(request.body)
        serializer = UserSerializer(data = data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data},status=201)
        return JsonResponse({"error":serializer.errors},status=400)
    except Exception as e:
        return JsonResponse({"error":str(e)},status=400)

@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"error":'invalid method'},status=400)
    try:
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        user = authenticate(username=email,password=password)
        if not user:
            return JsonResponse({"error":"please enter valid email and password"},status=400)
        
        return JsonResponse({"data":user},status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)},status=400)


    
    

