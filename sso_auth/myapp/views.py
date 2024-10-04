from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth import authenticate, login, logout
 
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Create your views here.
