from django.db import models


#Категория товара
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

# Модель Товара
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")

    title = models.CharField(max_length=100, verbose_name="Что за  товара")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
