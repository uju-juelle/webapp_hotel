from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("booking/", boooking_page, name="booking"),
    path("contact/", contact_page, name="contact"),
    path("room/", room_page, name="room"),
    path("service/", service_page, name="service"),
    path("team/", team_page, name="team"),
    path("testimonial/", testimonial_page, name="testimonial")
]