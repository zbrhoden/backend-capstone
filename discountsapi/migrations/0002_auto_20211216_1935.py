# Generated by Django 3.2.10 on 2021-12-16 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discountsapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='quantity',
        ),
    ]
