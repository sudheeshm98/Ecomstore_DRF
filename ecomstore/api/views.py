from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Smartphones, Cart
from .serializers import SmartphoneSerializer, CartSerializer


# Create your views here.


class ListSmartphones(generics.ListCreateAPIView):
    queryset = Smartphones.objects.all()
    serializer_class = SmartphoneSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = SmartphoneSerializer(queryset, many=True)
        return Response(serializer.data)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphones.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SmartphoneSerializer(queryset,many=False)
        return Response(serializer.data)

class UpdateView(generics.UpdateAPIView):
    queryset = Smartphones.objects.all()
    serializer_class = SmartphoneSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Smartphones.objects.all()
    serializer_class = SmartphoneSerializer


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try:
            product = Smartphones.objects.get(id=product_id)
            cart_item = Cart(user=request.user, product=product, quantity=quantity)
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

