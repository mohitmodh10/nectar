from django.contrib import admin
from django.urls import path
from home import userViewSet, productViewSet
from nectar import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userRegestration',userViewSet.UserViewSet.userRegistration),
    path('userLogin',userViewSet.UserViewSet.userLogin),
    path('userProfileUpdate',userViewSet.UserViewSet.userUpdate),
    path('addProduct',productViewSet.ProductViewSet.addProduct),
    path('getProduct',productViewSet.ProductViewSet.getProduct),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
