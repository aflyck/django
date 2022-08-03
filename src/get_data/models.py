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
