from django.urls import path
from .views import index, AddWine, Wines
from . import views

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('wines/', AddWine.as_view(), name='add_wine'),
    path('wine', Wines.as_view(), name='wines')
]
