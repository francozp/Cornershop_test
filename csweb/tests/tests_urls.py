from django.test import SimpleTestCase
from django.urls import reverse, resolve
from csweb.views import *

class TestUrls(SimpleTestCase): 
    # Test if the url are reacheable for all the views
    def test_home_url_is_resolved(self):
        url = reverse("Home")
        self.assertEquals(resolve(url).func.view_class, HomeView)
    
    def test_menu_url_is_resolved(self):
        url = reverse("Menu")
        self.assertEquals(resolve(url).func.view_class, MenuView)
    
    def test_detailmenu_url_is_resolved(self):
        url = reverse("detailMenu", args=["menu-id"])
        self.assertEquals(resolve(url).func.view_class, MenuDetailView)
    
    def test_register_url_is_resolved(self):
        url = reverse("Register")
        self.assertEquals(resolve(url).func.view_class, RegisterView)
    
    def test_option_url_is_resolved(self):
        url = reverse("Option")
        self.assertEquals(resolve(url).func.view_class, OptionView)
    
    def test_optionsdetail_url_is_resolved(self):
        url = reverse("OptionsDetail")
        self.assertEquals(resolve(url).func.view_class, SeeOptionsView)
    
    def test_menulist_url_is_resolved(self):
        url = reverse("MenuList")
        self.assertEquals(resolve(url).func.view_class, MenuListView)
    
    def test_editmenu_url_is_resolved(self):
        url = reverse("editMenu", args=["menu-id"])
        self.assertEquals(resolve(url).func.view_class, MenuEditView)
    
    def test_delete_url_is_resolved(self):
        url = reverse("delete", args=["option-id"])
        self.assertEquals(resolve(url).func.view_class,OptionDeleteView)
    
    def test_addmenuoption_url_is_resolved(self):
        url = reverse("addMenuOptions")
        self.assertEquals(resolve(url).func.view_class, AddOptionsView)