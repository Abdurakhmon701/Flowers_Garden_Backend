from django.db import models	


class CategoryModel(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='images/',blank=False)

	def __str__(self):
		return self.name


class ProductModel(models.Model):
	category = models.ForeignKey(CategoryModel,null=True,blank=True,on_delete=models.SET_NULL)
	product_name = models.CharField(max_length=150)
	product_description = models.TextField()
	product_photo = models.ImageField(upload_to='images/',)
	product_price = models.CharField(max_length=20)

	def __str__(self):
		return self.product_name

class BasketModel(models.Model):#korzina
	telegram_id = models.CharField(max_length=30)
	product_id = models.TextField()
	product_name = models.CharField(max_length=150)
	product_price = models.CharField(max_length=20)
	count = models.TextField()



class UserModel(models.Model):
	telegram_id = models.CharField(max_length=30)
	username = models.CharField(max_length=30)

class OrderModel(models.Model):
	telegram_id = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	telephone_number = models.CharField(max_length=20)
	location_x = models.
	location_y = models.

# startni bosganda UserModelga userni va username ni qo'shish kerak