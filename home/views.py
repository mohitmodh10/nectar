from home.commonResponse import generateCommonResponse
from rest_framework.decorators import api_view
from django.http import response
from .serializers import UserSerializer
from .models import UserModel
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class UserViewSet(viewsets.ModelViewSet):
    @api_view(['POST'])
    def userRegistration(request):
        user = UserModel.objects.filter(email=request.data["email"]).first()
        if user is None:    
            s = UserSerializer(data = request.data)
            if s.is_valid():
                s.save()
                user = UserModel.objects.filter(email=request.data["email"]).first()
                print(s.data)
                refresh = RefreshToken.for_user(user)
                data =  {
                    "status":1,
                    "message": "User saved successfully",
                    "data":s.data,
                    "token":str(refresh.access_token) 
                    }
                return response.JsonResponse(data)
            else:
                data = generateCommonResponse(0,"all fileds are required",s.data)
                return response.JsonResponse(data)
        else:
            data = generateCommonResponse(0,"user is already exists",[])
            return response.JsonResponse(data)

    

    @api_view(['POST'])
    def userLogin(request):
        user = UserModel.objects.filter(email=request.data["email"]).first()
        if user is not None:
            if check_password(request.data["password"],user.password,setter=None, preferred='default'):
                refresh = RefreshToken.for_user(user)
                print(UserSerializer(user).data)
                data =  {
                "status":1,
                "message": "Login successfully",
                "data":UserSerializer(user).data,
                "token":str(refresh.access_token) }
                return response.JsonResponse(data)
            else:
                data = generateCommonResponse(0,"wrong password",[])
                return response.JsonResponse(data)
        else:
            data = generateCommonResponse(0,"user not found",[])
            return response.JsonResponse(data)