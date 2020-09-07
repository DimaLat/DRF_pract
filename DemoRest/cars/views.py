from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()  # вынимать все данные из модели Car
    permission_classes = (IsAuthenticated, ) # просмотр только если авторизован IsAdminUser (только админу)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer  # указываем именно его потому что нужны все поля fields = '__all__'
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)  # указываем пермишен, что только админ может изменять удалять и тд
