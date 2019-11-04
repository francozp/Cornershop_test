from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="Home"),
    path("menu", views.MenuView.as_view(), name = "Menu"),
    path("menu/<pk>", views.MenuDetailView.as_view(), name="detailMenu"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='Register'),
    path('option', views.OptionView.as_view(), name = "Option"),
    path("usersoptions",views.SeeOptionsView.as_view(), name = "OptionsDetail"),
    path('menu_list', views.MenuListView.as_view(), name = "MenuList"),
    path('editMenu/<pk>',views.MenuEditView.as_view(),name="editMenu"),
    path('editMenu/delete/<pk>', views.OptionDeleteView.as_view(), name='delete'),
    path('addOptions',views.AddOptionsView.as_view(), name="addMenuOptions"),
]
# API URLS
urlpatterns += [
    path("api/getdishes", views.AjaxMenuView.as_view()),
    path("editMenu/api/getdishes", views.AjaxMenuView.as_view())]