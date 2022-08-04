from django.shortcuts import render
from .models import Vacancy


# Create your views here.

def home(request):
    vacancy = Vacancy.objects.all()
    return render(request,
                  'get_data/home.html',
                  {'object_list': vacancy})
