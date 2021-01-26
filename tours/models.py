from django.db import models


class Tours(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, verbose_name='Описание')
    picture = models.URLField(max_length=600, verbose_name='Ссылка на картинку')
    price = models.IntegerField(null=True, verbose_name='Стоимость')
    stars = models.IntegerField(null=True, verbose_name='Звёзды')
    country = models.CharField(max_length=100, verbose_name='Страна')
    nights = models.IntegerField(null=True, verbose_name='Длительность')
    date = models.CharField(max_length=50, verbose_name='Дата')
    departure = models.ForeignKey('Depart', on_delete=models.PROTECT, null=True, verbose_name='Отправление')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Depart(models.Model):
    title = models.CharField(verbose_name='Отправление', max_length=50)
    ru_departure = models.CharField(max_length=50, verbose_name='Отправление_RU', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отправление'
        verbose_name_plural = 'Отправления'
