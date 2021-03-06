# Generated by Django 3.1.1 on 2020-10-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_addvendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('manufac', models.CharField(max_length=50)),
                ('dealer', models.TextField()),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('pricerange', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Addunit',
        ),
    ]
