from django.shortcuts import render
from .models import CategoryModel,ProductModel,BasketModel
from .serializers import CategorySerializers,ProductSerializers,BasketSerializers,PUTBasketSerializers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status

class CategoryView(APIView):
	def get_object(self, pk):
		try:
			return CategoryModel.objects.get(pk=pk)
		except CategoryModel.DoesNotExist:
			raise Http404
	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = CategorySerializers(snippet)
		return Response(serializer.data)


class ProductView(APIView):
	def get_object(self, pk):
		result = ProductModel.objects.all().filter(category=pk)
		return result
	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = ProductSerializers(snippet,many=True)
		return Response(serializer.data)


class CategoryAllView(ModelViewSet):
	queryset = CategoryModel.objects.all()
	serializer_class = CategorySerializers


class ProductAllView(ModelViewSet):
	queryset = ProductModel.objects.all()
	serializer_class = ProductSerializers


class BasketView(ModelViewSet):
	queryset = BasketModel.objects.all()
	serializer_class = BasketSerializers


class BasketAllView(APIView):
	def get_object(self, pk):
		result = BasketModel.objects.all().filter(telegram_id=pk)
		return result
	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = BasketSerializers(snippet,many=True)
		return Response(serializer.data)


@api_view(['GET','DELETE'])
def delete_object(request, tel_id, pk):
	if request.method == 'DELETE':
		count = BasketModel.objects.filter(telegram_id=tel_id,product_id=pk)
		if count:
			count.delete()
			return Response({'message':"Mahsulot o'chirildi"})
		else:
			return Response({'message':"Mahsulot topilmadi"},status = status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		try:
			count = BasketModel.objects.get(telegram_id=tel_id,product_id=pk)
			if count:
				serializer = BasketSerializers(count)
				return Response(serializer.data)
		except:
			return Response({'message':"Mahsulot topilmadi"},status = status.HTTP_404_NOT_FOUND)




@api_view(['DELETE'])
def delete_objects_all(request, telegram_id):
	if request.method == 'DELETE':
		count = BasketModel.objects.filter(telegram_id=telegram_id)
		if count:
			count.delete()
			return Response({'message':"Mahsulot o'chirildi"})
	else:
		return Response({'message':"Mahsulot topilmadi"},status = status.HTTP_404_NOT_FOUND)




@api_view(['PUT'])
def put_object(request, tel_id, product):
	try:
		snippet = BasketModel.objects.get(telegram_id=tel_id,product_id=product)
		print("SSSSS",snippet)
	except BasketModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'PUT':
		serializer = PUTBasketSerializers(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	