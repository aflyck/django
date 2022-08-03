from django.contrib import admin
from .models import City, ProgramLanguage, Vacancy
# Register your models here.


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    prepopulated_fields = {'slug': ["name"]}


@admin.register(ProgramLanguage)
class AdminProgramLanguage(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Vacancy)
class AdminVacancy(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
