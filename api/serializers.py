from rest_framework import serializers
from api.models import CategoryModel,ProductModel,BasketModel

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