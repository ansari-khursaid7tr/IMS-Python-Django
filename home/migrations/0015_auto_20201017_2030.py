# Generated by Django 3.1.1 on 2020-10-17 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20201017_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='company',
            name='tagline',
        ),
    ]
