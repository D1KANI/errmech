# Generated by Django 3.2.8 on 2021-10-25 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('content', models.CharField(max_length=64, verbose_name='Значение')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('short_desc', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('desc', models.TextField(blank=True, verbose_name='Описание')),
                ('basic_price', models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Основная цена')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Ссылка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.category', verbose_name='Категория')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.company', verbose_name='Компания')),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Цена')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.company', verbose_name='Компания')),
            ],
            options={
                'ordering': ['company'],
            },
        ),
        migrations.CreateModel(
            name='ProductCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.characteristic', verbose_name='Характеристика')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product', verbose_name='Продукт')),
            ],
            options={
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product', verbose_name='Продукт')),
            ],
            options={
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='KeyboardSwitches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product', verbose_name='Товар')),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.switch', verbose_name='Переключатель')),
            ],
            options={
                'ordering': ['keyboard'],
            },
        ),
    ]
