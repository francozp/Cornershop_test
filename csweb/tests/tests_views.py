from django.test import TestCase, Client
from django.urls import reverse
from csweb.models import *
import datetime
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # urls for the test
        self.home_url = reverse("Home")
        self.menu_url = reverse("Menu")
        self.menu_list_url = reverse("MenuList")
        self.detail_menu_url = reverse("detailMenu", args=[1])
        self.register_url = reverse("Register")
        self.user_option_url = reverse("OptionsDetail")
        self.option_url = reverse("Option")
        self.editmenu_url = reverse("editMenu", args=[1])
        self.delete_url = reverse("delete", args=[1])
        self.addoptions_url = reverse("addMenuOptions")
        # objects for the test
        self.user = User.objects.create_user("test_user", '', "test")
        self.profile = Profile.objects.create(user_id = self.user.id, name= "test_profile", privileges=True)
        self.menu = Menu.objects.create(menu_id = 1, fecha = datetime.date.today())
        self.maindish = MainDish.objects.create(main_id = 1, description = "test_dish")
        self.option = Options.objects.create(option_id = 1, main_id = 1, menu_id = 1, salad = True, dessert = True,menu_option=1)

    # Test GET method for all the views
    def test_home_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "index.html")

    def test_menu_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.menu_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "menu.html")

    def test_detailmenu_GET(self):
        response = self.client.get(self.detail_menu_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "menu_detail.html")

    def test_register_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "register.html")

    def test_option_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.option_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "option.html")
    
    def test_user_options_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.user_option_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "seeOptions.html")

    def test_menu_list_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.menu_list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "menulist.html")
    
    def test_editmenu_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.editmenu_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "menuEdit.html")
    
    def test_delete_GET(self):
        self.client.login(username='test_user', password='test')
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "delete.html")

    # Test POST method
    def test_menu_create_dish_POST(self):
        self.client.login(username='test_user', password='test')
        response = self.client.post(self.menu_url, {
            "form-0-newdish": "test_dish_2",
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '1',
            'form-MIN_NUM_FORMS': '0', 
            'form-MAX_NUM_FORMS': '1000'
        })
        self.assertEquals(response.status_code,200)
        self.assertEquals(len(MainDish.objects.all()),2)

    def test_menu_create_POST(self):
        self.client.login(username='test_user', password='test')
        response = self.client.post(self.menu_url, {
            "form-0-maindish": "test_dish",
            "form-0-salad": "on",
            "form-0-dessert": "on",
            "date": "03/11/2019",
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '1',
            'form-MIN_NUM_FORMS': '0', 
            'form-MAX_NUM_FORMS': '1000'
        })
        self.assertEquals(response.status_code,200)
        self.assertEquals(len(Menu.objects.all()),2)

    def test_editmenu_POST(self):
        self.client.login(username='test_user', password='test')
        response = self.client.post(self.option_url, {
            "option_id": 1,
            "maindish": "test_dish",
            "salad": "on",
            "dessert": "on",
        })
        self.assertEquals(response.status_code,200)
        self.assertEquals(str(self.option.main_id), MainDish.objects.get(description="test_dish").main_id)
    
    
    def test_register_POST(self):
        self.client.login(username='test_user', password='test')
        response = self.client.post(self.register_url, {
            "username": "test",
            "password": "password",
            "confirm_password": "password",
            "privilege": 'on',
            "name": "Test",
        })
        user = User.objects.get(username="test")
        profile = Profile.objects.get(name="Test")
        self.assertEquals(response.status_code,200)
        self.assertEquals(user.id, profile.user_id)

    def test_option_POST(self):
        self.client.login(username='test_user', password='test')
        response = self.client.post(self.option_url, {
            "option": self.option.option_id,
            "detail": ""
        })
        user_option = UserOption.objects.get(option_id = self.option.option_id)
        self.assertEquals(response.status_code,302)
        self.assertEquals(user_option.user_id, self.user.id)

    def test_addoptions_POST(self):
        self.client.login(username='test_user', password='test')
        response = self.client.post(self.addoptions_url, {
            "addOption": 1
        })
        self.assertEquals(response.status_code,200)
        response = self.client.post(self.addoptions_url, {
            "form-0-maindish": "test_dish",
            "form-0-salad": "on",
            "form-0-dessert": "on",
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '1',
            'form-MIN_NUM_FORMS': '0', 
            'form-MAX_NUM_FORMS': '1000'
        })
        self.assertEquals(response.status_code,200)
        self.assertEquals(Options.objects.first().main_id, str(self.maindish.main_id))