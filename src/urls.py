"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api.views import CategoryView,ProductView,\
CategoryAllView,ProductAllView,BasketView,BasketAllView,delete_object,delete_objects_all

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category',CategoryAllView),
router.register('get_product',ProductAllView),
router.register('basket',BasketView)



urlpatterns = [
    path('',include(router.urls)),  
    path('admin/', admin.site.urls),
    path('category/<int:pk>/',CategoryView.as_view()),
    path('product/<int:pk>/',ProductView.as_view()),
    path('basket_all/<int:pk>/',BasketAllView.as_view()),
    path('basket_delete/<str:tel_id>/<str:pk>/',delete_object),
    path('basket_delete_all/<str:telegram_id>/',delete_objects_all)

]+static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)