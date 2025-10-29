from django.urls import path
from . import views

# Create your views here.



urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('courses', views.courses),
]
