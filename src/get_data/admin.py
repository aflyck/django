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
    list_display = ['title', 'company', 'program_language', 'description', 'city', 'url']
    search_fields = ['company', 'city', 'program_language']
    prepopulated_fields = {'slug': ['title']}
