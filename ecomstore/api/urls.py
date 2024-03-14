from django.urls import path
from .views import ListSmartphones, DetailView, UpdateView, DeleteView, AddToCartView
from . import views

urlpatterns = [
    path('smartphones/', ListSmartphones.as_view(), name='smartphones'),
    path('details/<int:pk>/', DetailView.as_view(), name='details'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart')


]
