from rest_framework import serializers
from api.models import CategoryModel,ProductModel

class CategorySerializers(serializers.ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = '__all__'