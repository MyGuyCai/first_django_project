from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog_index'),
    path('about_us', views.about_us, name="about_us"),
    path('services', views.services, name="services"),
    path('contact_us', views.contact_us, name="contact_us")
]
