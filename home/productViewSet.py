from django.shortcuts import render
from home.commonResponse import generateCommonResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.http import response
from rest_framework.serializers import Serializer
from .serializers import ProductSeriaizer
from .models import ProductModel
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    @api_view(['POST'])
    def addProduct(request):
        s = ProductSeriaizer(data = request.data)
        if s.is_valid():
            s.save()
            data = generateCommonResponse(1,"product added successfully",s.data)
            return response.JsonResponse(data)
        else:
            data = generateCommonResponse(0,"all fileds are required",s.data)
            return response.JsonResponse(data)