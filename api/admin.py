from django.contrib import admin
from .models import *
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(BasketModel)
# Register your models here.
