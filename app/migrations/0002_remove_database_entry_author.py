# Generated by Django 2.2.12 on 2022-04-27 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database_entry',
            name='author',
        ),
    ]
