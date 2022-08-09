from django.shortcuts import render
from .models import Vacancy
from .forms import FinderForm

# Create your views here.


def home(request):
    form = FinderForm()
    city = request.GET.get('city')
    language = request.GET.get('program')
    data_dict = {}
    if city:
        # __имя_поля берется из связанной таблицы в данном случае __slug
        data_dict['city__slug'] = city
    if language:
        data_dict['program_language__slug'] = language
    vacancy = Vacancy.objects.filter(**data_dict)

    return render(request,
                  'get_data/home.html',
                  {'object_list': vacancy,
                   'form': form})
