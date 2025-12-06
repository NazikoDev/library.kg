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

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name="Книга")

    text = models.TextField(
        verbose_name="Текст отзыва",
        validators=[
            MinLengthValidator(200, message="Минимум 200 символов!")
        ]
    )
    stars = models.PositiveIntegerField(
        verbose_name="Оценка",
        validators=[
            MinValueValidator(1, message="Ставьте оценку от 1 до 5"),
            MaxValueValidator(5, message="Ставьте оценку от 1 до 5")
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.book.title} - {self.stars} звезд"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
