from django.shortcuts import render
from .models import CategoryModel,ProductModel,BasketModel,UserModel,OrderModel
from .serializers import CategorySerializers,ProductSerializers,BasketSerializers,PUTBasketSerializers,UserSerializers,OrderSerializers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse



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


@api_view(['GET','DELETE','PUT'])
def delete_object(request, tel_id, pk):
	try:
		snippet = BasketModel.objects.get(telegram_id=tel_id,product_id = pk)
	except BasketModel.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

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
	if request.method == "PUT":
		serializer = PUTBasketSerializers(snippet,data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	return Response({'message':'Surovlar mos emas'},status=status.HTTP_400_BAD_REQUEST)





@api_view(['DELETE'])
def delete_objects_all(request, telegram_id):
	if request.method == 'DELETE':
		count = BasketModel.objects.filter(telegram_id=telegram_id)
		if count:
			count.delete()
			return Response({'message':"Mahsulot o'chirildi"})
		else:
			return Response({'message':"Mahsulot topilmadi"},status = status.HTTP_404_NOT_FOUND)




class UserView(APIView):
	def post(self, request, format=None):
		serializer = UserSerializers(data = request.data)
		# print(serializer.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get yozish apiga f-yasini ham va tekshirish, kegin bazaga qosh postni ishlatish


@api_view(['GET'])
def get_user(request, telegram_id):
	try: 
		telegram_id = UserModel.objects.get(telegram_id=telegram_id) 
	except UserModel.DoesNotExist:
		return Response({'message':"User topilmadi"}, status=status.HTTP_404_NOT_FOUND) 
	if request.method == 'GET':
		serializer = UserSerializers(telegram_id)
		return Response(serializer.data)


# Order ni post qilish uchun klass


class OrderPostView(ModelViewSet):
	queryset = OrderModel.objects.all()
	serializer_class = OrderSerializers


# class OrderView(APIView):
# 	def post(self, request, format=None):
# 		serializer = OrderSerializers(data = request.data)
# 		# print(serializer.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# Order ni GET qilish uchun klass va decorator
# class OrderAllView(APIView):
# 	def get_object(self, pk):
# 		result = OrderModel.objects.all().filter(telegram_id=pk)
# 		return result
# 	def get(self, request, pk):
# 		snippet = self.get_object(pk)
# 		serializer = OrderSerializers(snippet,many=True)
# 		return Response(serializer.data)

# @api_view(['GET'])
# def get_information_from_order(request, telegram_id):
# 	try: 
# 		telegram_id = OrderModel.objects.get(telegram_id=telegram_id) 
# 	except OrderModel.DoesNotExist:
# 		return Response({'message':"Userga tegishli ma'lumotlar topilmadi"}, status=status.HTTP_404_NOT_FOUND) 
# 	if request.method == 'GET':
# 		serializer = OrderSerializers(telegram_id)
# 		return Response(serializer.data)