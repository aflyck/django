from django.shortcuts import render
import datetime


def home(request):
    name = "Alexey"
    data = datetime.datetime.now().date()
    return render(request, 'home.html', context={
        'name': name,
        "data": data
    })
