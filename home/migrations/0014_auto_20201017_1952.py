# Generated by Django 3.1.1 on 2020-10-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='tagline',
            field=models.CharField(max_length=50, null=True),
        ),
    ]