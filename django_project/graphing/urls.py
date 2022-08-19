from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='graphing_index'),
]
