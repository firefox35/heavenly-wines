from django.urls import path
from .views import index, AddWine, Wines, WineDetail, DeleteWine, EditWine
from . import views

urlpatterns = [
    path("", index.as_view(), name="home"),
    path("wines/", AddWine.as_view(), name="add_wine"),
    path("wines", Wines.as_view(), name="wines"),
    path("<slug:pk>/", WineDetail.as_view(), name="wine_detail"),
    path("delete/<slug:pk>/", DeleteWine.as_view(), name="delete_wine"),
    path("edit/<slug:pk>/", EditWine.as_view(), name="edit_wine"),
]
