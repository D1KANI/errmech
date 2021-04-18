from django.db import models
from django.urls import reverse


class Company(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['title']


class CompanySwitches(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Компания Переключателей'
        verbose_name_plural = 'Компании Переключателей'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')
    image = models.ImageField(upload_to='photos/categories/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Item(models.Model):
    category_fk = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    company_fk = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
    name = models.CharField(unique=True, max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')
    price = models.IntegerField(verbose_name='Базовая цена')
    desc_small = models.TextField(verbose_name='Короткое описание')
    desc = models.TextField(verbose_name='Описание')
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Основная фотография', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        template = '{0.company_fk} {0.name}'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('ViewItem', kwargs={"item_slug": self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['company_fk']


class ItemWithPhoto(models.Model):
    item_fk = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')

    def __str__(self):
        template = '{0.item_fk} {0.photo}'
        return template.format(self)

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['item_fk']


class ItemCharacteristic(models.Model):
    item_fk = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    title = models.CharField(max_length=50, verbose_name='Характеристика')
    content = models.CharField(max_length=50, verbose_name='Значение')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        ordering = ['item_fk']


class Switch(models.Model):
    company_fk = models.ForeignKey(CompanySwitches, on_delete=models.CASCADE, verbose_name='Компания')
    title = models.CharField(max_length=50, verbose_name='Название')
    color = models.CharField(max_length=10, verbose_name='Цвет')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена переключателя')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Переключатель'
        verbose_name_plural = 'Переключатели'
        ordering = ['company_fk']


class KeyboardSwitches(models.Model):
    item_fk = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Клавиатура')
    switch_fk = models.ForeignKey(Switch, on_delete=models.CASCADE, verbose_name='Переключатель')
    count = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        template = '{0.item_fk} {0.switch_fk}'
        return template.format(self)

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Переключатель клавиатур'
        verbose_name_plural = 'Переключатели клавиатур'
        ordering = ['item_fk']


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    short_desc = models.TextField(verbose_name='Описание')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']
