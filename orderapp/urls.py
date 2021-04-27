
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('addcart/<int:id>', v.addtocart,name='addcart'),
]
