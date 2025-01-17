from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def create_product(request):
    if request.method != 'POST':
        return JsonResponse({"error":'invalid method'},status=400)
    try:
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data},status=201)
        
        return JsonResponse({"error":serializer.errors},status=400)
    
    except Exception as e:
        return JsonResponse({"error":str(e)},status=400)


@csrf_exempt
def get_all_product(request):
    if request.method != 'GET':
        return JsonResponse({"error": 'Invalid method'}, status=400)
    
    try:
        products = Product.objects.all()
        if not products.exists():
            return JsonResponse({"error": "No products found"}, status=404)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({"data": serializer.data}, status=200)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
