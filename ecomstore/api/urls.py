from django.urls import path
from .views import ListSmartphones
from . import views

urlpatterns = [
    path('smartphones/', ListSmartphones.as_view(), name='smartphones')

]
