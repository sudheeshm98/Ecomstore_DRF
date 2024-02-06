from rest_framework import serializers
from .models import Smartphones

class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphones
        fields = '__all__'

