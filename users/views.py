from django.shortcuts import render
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

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
        
        token,_ = Token.objects.get_or_create(user=user)
        return JsonResponse({"token":str(token.key)},status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)},status=400)


    
    

