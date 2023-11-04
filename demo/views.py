import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import shoes
# Create your views here.


def index(request):
   with open("./static/data/shoes.json") as f:
    data = json.load(f)
    for product in data["shoes"]:
        Shoes =shoes(name = product['name'],id = product['id'], price = product['price'],image = product['image'], color = product['color'], description = product['description'])
        Shoes.save()
   
    Shoes = shoes.objects.all()
    return render(request, "index.html", {"Shoes": Shoes})