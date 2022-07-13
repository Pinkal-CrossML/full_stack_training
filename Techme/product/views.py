from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        user_count = Product.objects.all()
        serializer = ProductSerializer(user_count, many=True)

        # content = {'category': }
        return Response({'category': serializer.data})

