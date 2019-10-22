# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MainDish(models.Model):
    main_id = models.CharField(primary_key=True, max_length=16)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'main_dish'


class Menu(models.Model):
    menu_id = models.CharField(primary_key=True, max_length=16)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'menu'


class Options(models.Model):
    option_id = models.CharField(primary_key=True, max_length=16)
    main = models.ForeignKey(MainDish, models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)
    salad = models.IntegerField()
    dessert = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'options'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=16)
    admin = models.IntegerField()
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'


class UserOption(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    option = models.ForeignKey(Options, models.DO_NOTHING)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_option'