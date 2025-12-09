from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    image = models.ImageField(upload_to='books/', verbose_name="Обложка книги", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

