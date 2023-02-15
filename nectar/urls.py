from django.contrib import admin
from django.urls import path
from home import userViewSet
from nectar import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userRegestration',userViewSet.UserViewSet.userRegistration),
    path('userLogin',userViewSet.UserViewSet.userLogin),
    path('userProfileUpdate',userViewSet.UserViewSet.userUpdate),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
