from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Название')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Компания')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    short_desc = models.TextField(verbose_name='Короткое описание', blank=True)
    desc = models.TextField(verbose_name='Описание', blank=True)
    basic_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Основная цена', default=1)
    slug = models.SlugField(unique=True, verbose_name='Ссылка', max_length=64)

    def __str__(self):
        return f'{self.category.title} : {self.company.title} - {self.title}'


class Company(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Название')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=64, verbose_name='Ссылка', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Photos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return f'{self.product.title} : {self.image.url}'

    class Meta:
        ordering = ['product']


class Switch(models.Model):
    company = models.ForeignKey('Company', verbose_name='Компания', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', default=0)

    def __str__(self):
        return f'{self.company} {self.title}'

    class Meta:
        ordering = ['company']


class KeyboardSwitches(models.Model):
    keyboard = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    switch = models.ForeignKey(Switch, verbose_name='Переключатель', on_delete=models.CASCADE)
    count = models.IntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.keyboard} {self.switch}'

    class Meta:
        ordering = ['keyboard']


class Characteristic(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    content = models.CharField(max_length=64, verbose_name='Значение')

    def __str__(self):
        return f'{self.title} {self.content}'

    class Meta:
        ordering = ['title']


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, verbose_name='Характеристика', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} {self.characteristic}'

    class Meta:
        ordering = ['product']
