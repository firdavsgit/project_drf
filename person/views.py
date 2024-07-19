from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from person.models import Food
from person.permissions import IsOwnerUserOrReadOnly, IsAdminUserOrReadOnly
from person.serializers import FoodSerializers, CategorySerializers


class Createfood(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class listfood(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]

class Updatefood(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsOwnerUserOrReadOnly]
    authentication_classes = [TokenAuthentication]


class deletefood(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

class createcategory(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]

class listcategory(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers


class Updatecategory(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsOwnerUserOrReadOnly]
    authentication_classes = [TokenAuthentication]


class deletecategory(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]