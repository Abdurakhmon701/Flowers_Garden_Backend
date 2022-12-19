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

	def __str__(self):
		return self.telegram_id

 

class UserModel(models.Model):
	telegram_id = models.CharField(max_length=30)
	username = models.CharField(max_length=30)

	def __str__(self):
		return self.username

class OrderModel(models.Model):
	Status = (
				("Y","Yangi"),
				("M","Moderatsiya"),
				("T","Tasdiqlangan"),
				("B","Bekor qilingan"),
			)
	address = models.TextField()
	user_phone = models.CharField(max_length=15)
	payment = models.CharField(max_length=10)
	order_id = models.CharField(max_length=250)
	products = models.TextField()
	products_price = models.CharField(max_length=200)
	user_name = models.CharField(max_length=50,blank=True)
	status = models.CharField(default='Y',choices=Status,max_length=1,blank=True)
	telegram_id = models.CharField(max_length=15)
	telegram_username = models.CharField(max_length=100,blank=True)
	phone_number = models.CharField(max_length=15)

	# def __str__(self):
	# 	order_information = f"{self.username},{self.telegram_id},{self.telephone_number},{self.location_x},{self.location_y}"
	# 	return order_information

# startni bosganda UserModelga userni va username ni qo'shish kerak