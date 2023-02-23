from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    """Класс модели категорий"""
    title = models.CharField(
        max_length=50,
        verbose_name='Название категории'
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(
        max_length=200,
        verbose_name='Описание категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']
    
    def __str__(self) -> str:
        return self.title

class Status(models.Model):
    """Класс модели статусов заявок"""
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['pk']


class App(models.Model):
    """Класс модели заявок"""
    title = models.CharField(max_length=50, verbose_name='Название заявки')
    text = models.TextField(max_length=500, verbose_name='Текст заявки')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Автор заявки'
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    status = models.ForeignKey(
        Status,
        default=1,
        on_delete=models.SET_DEFAULT,
        verbose_name='Статус завки'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-pub_date']
    
    def __str__(self) -> str:
        return self.title[:20]
