from django.shortcuts import render
from .models import *
# Create your views here.


def home_page(request):
    products = Products.objects.all()
    services = Category.objects.all()
    reviews = Reviews.objects.all()
    context = {
        "products" : products,
        "services": services,
        "reviews": reviews
    }


    return render(request, "Hotel/index.html", context)