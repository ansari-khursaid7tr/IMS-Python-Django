# Generated by Django 3.1.1 on 2020-10-18 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20201018_1708'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PriceRange',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]