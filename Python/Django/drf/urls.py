"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, ProductViewSet2, ProductViewSet3


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'products2', ProductViewSet2, basename='products2')
router.register(r'products3', ProductViewSet3, basename='products3')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
