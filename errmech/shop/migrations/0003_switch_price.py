# Generated by Django 3.2 on 2021-04-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210416_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена переключателя'),
        ),
    ]
