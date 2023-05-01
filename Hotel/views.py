from django.shortcuts import render
from .models import *
# Create your views here.


def home_page(request):
    products = Products.objects.all()
    context = {
        "products" : products
    }


    return render(request, "Hotel/index.html", context)