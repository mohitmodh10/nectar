from django.shortcuts import render
from home.commonResponse import generateCommonResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.http import response
from rest_framework.serializers import Serializer
from .serializers import ProductSeriaizer, ProductImageSerializer
from .models import ProductModel,ProductImagesModel
from rest_framework import viewsets
from django.http import QueryDict


def addProductImages(request,s):
        imageList = []
        for i in request.data.getlist('product_images'):
            ordinary_dict = {'product_image':i,'product_id':s.data['id']}
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)
            image = ProductImageSerializer(data = query_dict)
            if image.is_valid():
                image.save()
                imageList.append(image.data['product_image'])
            else:
                print("image data is not valid")
        print(imageList)
        return imageList


class ProductViewSet(viewsets.ModelViewSet):
    @api_view(['POST'])
    def addProduct(request):
        if 'product_images' in request.data.keys() :
            s = ProductSeriaizer(data = request.data)
            if s.is_valid():
                s.save()
                imageList = addProductImages(request,s)
                for i in imageList:
                    s.data['product_images'].append(i)
                data = generateCommonResponse(1,"product added successfully",s.data)
                return response.JsonResponse(data)
            else:
                data = generateCommonResponse(0,"all fileds are required",s.data)
                return response.JsonResponse(data)
        else:
            data = generateCommonResponse(0,"product image is missing",[])
            return response.JsonResponse(data)
        
    
    @api_view(['GET'])
    def getProduct(request):
        queryset = ProductModel.objects.all()
        s = ProductSeriaizer(queryset,many = True)
        data = generateCommonResponse(1,"Success",s.data)
        return response.JsonResponse(data)
        # except:
        #     data = generateCommonResponse(1,"Success",[])
        #     return response.JsonResponse(data)
        
    
    @api_view(['GET'])
    def getProductImages(request):
        queryset = ProductImagesModel.objects.all()
        s = ProductImageSerializer(queryset,many = True)
        data = generateCommonResponse(1,"Success",s.data)
        return response.JsonResponse(data)