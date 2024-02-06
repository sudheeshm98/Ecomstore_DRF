from django.shortcuts import render
from rest_framework.response import Response

from .models import Smartphones
from .serializers import SmartphoneSerializer
from rest_framework.generics import ListCreateAPIView


# Create your views here.


class ListSmartphones(ListCreateAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphones.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response({'object_list': queryset})
