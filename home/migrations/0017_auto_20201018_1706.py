# Generated by Django 3.1.1 on 2020-10-18 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20201018_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricerange', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='pricerange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pricerange'),
        ),
    ]
