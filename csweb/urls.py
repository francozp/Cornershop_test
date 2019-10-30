from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="Home"),
    path("menu", views.MenuView.as_view(), name = "Menu"),
    path("menu", views.MenuView.as_view(), name = "newDish"),
    path("menu/<pk>", views.MenuDetailView.as_view(), name="detailMenu")
]
# API URLS
urlpatterns += [
    path("api/getdishes", views.AjaxMenuView.as_view())]