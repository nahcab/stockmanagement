# Generated by Django 3.1.2 on 2020-10-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201023_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='-', max_length=100),
        ),
    ]