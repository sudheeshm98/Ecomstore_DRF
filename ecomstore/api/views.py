from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .models import Smartphones
from .serializers import SmartphoneSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.


class ListSmartphones(ListCreateAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphones.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SmartphoneSerializer(queryset, many=True)
        return Response(serializer.data)

class DetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphones.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SmartphoneSerializer(queryset,many=False)
        return Response(serializer.data)

