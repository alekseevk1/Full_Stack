from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фотография")
    is_Ready = models.BooleanField(default=True)
    price = models.IntegerField(verbose_name="Цена")
    amount = models.IntegerField(verbose_name="Количество")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    description = models.TextField(blank=True, verbose_name="Описание")
    action = models.BooleanField(default=False, verbose_name="Акция")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['time_create', 'title']


  
class Category(models.Model):
    name = models.CharField(max_length=70, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
