from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
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


class App(models.Model):
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
        #default=Category.objects.get(pk=1)
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-pub_date']
