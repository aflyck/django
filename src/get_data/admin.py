from django.contrib import admin
from .models import City, ProgramLanguage
# Register your models here.


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    prepopulated_fields = {'slug': ["name"]}


@admin.register(ProgramLanguage)
class AdminProgramLanguage(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
