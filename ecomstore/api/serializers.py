from rest_framework import serializers
from .models import Smartphones,Cart

class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphones
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
