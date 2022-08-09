import datetime

from django.db import models


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Наименование населенного пункта",
                            unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Наименование населенного пункта'
        verbose_name_plural = "Наименование населенных пунктов"


class ProgramLanguage(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Язык программирования",
                            unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = "Языки программирования"


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Заголовок вакансии")
    company = models.CharField(max_length=250, verbose_name="Компания")
    description = models.TextField(verbose_name="Описание вакансии")
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name="Город")
    program_language = models.ForeignKey('ProgramLanguage', on_delete=models.CASCADE,
                                         verbose_name="Язык программирования")
    slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.city}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
