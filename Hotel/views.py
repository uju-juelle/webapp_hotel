from django.shortcuts import render
from .models import *
# Create your views here.


def home_page(request):
    products = Products.objects.all()
    services = Category.objects.all()
    reviews = Reviews.objects.all()
    staffs = Staff.objects.all()
    context = {
        "products" : products,
        "services": services,
        "reviews": reviews,
        "staffs": staffs
    }

    return render(request, "Hotel/index.html", context)



def about_page(request):
    staffs = Staff.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "Hotel/about.html", context)



def boooking_page(request):
    return render(request, "Hotel/booking.html")



def contact_page(request):
    return render(request, "Hotel/contact.html")



def room_page(request):
    products = Products.objects.all()
    reviews = Reviews.objects.all()
    context = {
        "products": products,
        "reviews": reviews
    }
    return render(request, "Hotel/room.html", context)



def service_page(request):
    services = Category.objects.all()
    reviews = Reviews.objects.all()
    context = {
        "services": services,
        "reviews": reviews
    }
    return render(request, "Hotel/service.html", context)



def team_page(request):
    return render(request, "Hotel/team.html")



def testimonial_page(request):
    return render(request, "Hotel/testimonial.html")