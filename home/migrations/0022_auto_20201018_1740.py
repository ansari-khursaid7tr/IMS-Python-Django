# Generated by Django 3.1.1 on 2020-10-18 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20201018_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ram'),
        ),
    ]