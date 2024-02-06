from django.urls import path
from .views import ListSmartphones, DetailView
from . import views

urlpatterns = [
    path('smartphones/', ListSmartphones.as_view(), name='smartphones'),
    path('details/<int:pk>/', DetailView.as_view(), name='details')


]
