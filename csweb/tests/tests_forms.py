from django.test import SimpleTestCase
from csweb.forms import *

class TestForms(SimpleTestCase):
    # Test if the forms are valid or not, depending on the data submitted
    def test_menu_form_valid_data(self):
        form = MenuForm(data={
            'maindish':'dish1',
            'salad': True,
            'dessert': True,
        })
        self.assertTrue(form.is_valid())
    
    def test_menu_form_no_data(self):
        form = MenuForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
    
    def test_modal_form_valid_data(self):
        form = ModalForm(data={
            'newdish':'dish1',
        })
        self.assertTrue(form.is_valid())
    
    def test_modal_form_no_data(self):
        form = ModalForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
    
    def test_option_form_valid_data(self):
        form = OptionForm(data= {
            'option': 1,
            'detail':'test_detail'
        })
        form.fields["option"].choices = [(1,"value")]
        self.assertTrue(form.is_valid())
    
    def test_option_form_no_data(self):
        form = OptionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'name': 'test_name',
            'privilege': True,
            'username':'test_user',
            'password':'test_password',
            'confirm_password': 'test_password'
        })
        self.assertTrue(form.is_valid())
        
    
    def test_user_registration_form_no_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
        