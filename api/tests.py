

# Test qilib ko'rish uchun nima kelayotganini 
import requests 
import json 

url = "http://127.0.0.1:8000"

def get_category_id(idi):
	http = f"{url}/category/{idi}"
	req = requests.get(http)
	data = json.loads(req.text)
	print(data)

# get_category_id(3)

def get_product_by_category(idi):
	http = f"{url}/product/{idi}"
	req = requests.get(http)
	data = json.loads(req.text)
	print(data)
	
# get_product_by_category(2)