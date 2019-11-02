from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="Home"),
    path("menu", views.MenuView.as_view(), name = "Menu"),
    path("menu/<pk>", views.MenuDetailView.as_view(), name="detailMenu"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='Register'),
    path('option', views.OptionView.as_view(), name = "Option"),
    path("usersoptions",views.SeeOptionsView.as_view(), name = "OptionsDetail")
]
# API URLS
urlpatterns += [
    path("api/getdishes", views.AjaxMenuView.as_view())]