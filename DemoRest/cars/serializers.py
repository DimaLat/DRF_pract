from rest_framework import serializers
from cars.models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # дефолт юзером будет админ, менять мы не сможем

    class Meta:
        model = Car  # указываем модель к которой сериализатор будет привязан
        fields = '__all__'  # указываем, что работаем (сериаллизуем) со всеми полями


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')
