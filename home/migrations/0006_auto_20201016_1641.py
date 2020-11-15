# Generated by Django 3.1.1 on 2020-10-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201015_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addunit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('manufac', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='CreateAccount',
        ),
    ]