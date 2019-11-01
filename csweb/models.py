# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CeleryTaskmeta(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celery_taskmeta'


class CeleryTasksetmeta(models.Model):
    taskset_id = models.CharField(unique=True, max_length=255)
    result = models.TextField()
    date_done = models.DateTimeField()
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'celery_tasksetmeta'


class MainDish(models.Model):
    main_id = models.CharField(primary_key=True, max_length=36)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'main_dish'


class Menu(models.Model):
    menu_id = models.CharField(primary_key=True, max_length=36)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'menu'


class Options(models.Model):
    option_id = models.CharField(primary_key=True, max_length=36)
    main = models.ForeignKey(MainDish, models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)
    salad = models.IntegerField()
    dessert = models.IntegerField()
    menu_option = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'options'


class Profile(models.Model):
    user_id = models.CharField(primary_key=True, max_length=36)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    privileges = models.IntegerField()
    name = models.CharField(max_length=100)
    rut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile'


class UserOption(models.Model):
    user = models.ForeignKey(Profile, models.DO_NOTHING)
    option = models.ForeignKey(Options, models.DO_NOTHING)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_option'
