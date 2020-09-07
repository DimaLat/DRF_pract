from django.contrib import admin
from django.urls import path, include
from cars.views import *

app_name = 'car'
urlpatterns = [
    path('/car/create', CarCreateView.as_view()),  # не хватало / в 'car/create'
    path('/all/', CarListView.as_view()),
    path('/car/detail/<int:pk>/', CarDetailView.as_view()), # int:pk берет из адрессной строки параметр, достает нужную запись
]
