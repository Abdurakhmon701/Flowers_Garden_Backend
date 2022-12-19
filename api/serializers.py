from rest_framework import serializers
from api.models import CategoryModel,ProductModel,BasketModel,UserModel,OrderModel

class CategorySerializers(serializers.ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
	class Meta:
		model = ProductModel
		fields = '__all__'

class BasketSerializers(serializers.ModelSerializer):
	class Meta:
		model = BasketModel
		fields = '__all__'

class PUTBasketSerializers(serializers.ModelSerializer):
	class Meta:
		model = BasketModel
		fields = ['count']

class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
	class Meta:
		model = OrderModel
		fields = '__all__'

	def create(self, validated_data):
		return OrderModel.objects.create(**validated_data)

# class BasketSerializersForPayment(serializers.ModelSerializer):
# 	class Meta:
# 		model = BasketModel
# 		fields = ['product_name']