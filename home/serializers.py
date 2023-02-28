from rest_framework import serializers
from .models import UserModel,ProductModel,ProductImagesModel
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    def create(self, validated_data):
        user = UserModel(
        email=validated_data['email'],
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        profile_image = validated_data['profile_image'],
        password = make_password(password=validated_data['password'],hasher='default', salt=None),)
        user.save()
        return user
    

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImagesModel
        fields = "__all__"


class ProductSeriaizer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only = True)
    class Meta:
        model = ProductModel
        fields = ['id','product_name','product_dic','product_price','product_discount_price','product_type','product_images']