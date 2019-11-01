# Generated by Django 2.2.2 on 2019-11-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryTaskmeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(max_length=50)),
                ('result', models.TextField(blank=True, null=True)),
                ('date_done', models.DateTimeField()),
                ('traceback', models.TextField(blank=True, null=True)),
                ('hidden', models.IntegerField()),
                ('meta', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'celery_taskmeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CeleryTasksetmeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskset_id', models.CharField(max_length=255, unique=True)),
                ('result', models.TextField()),
                ('date_done', models.DateTimeField()),
                ('hidden', models.IntegerField()),
            ],
            options={
                'db_table': 'celery_tasksetmeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('privileges', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('rut', models.IntegerField()),
            ],
            options={
                'db_table': 'profile',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
