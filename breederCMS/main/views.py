from django.shortcuts import render
from .models import AnimalEntry


def index(request):
    return render(request, 'main/base.html')


def about_breeder(request):
    return render(request, 'main/base_about-breeder.html')


def about_animal(request):
    return render(request, 'main/base_about-species.html')


def contact(request):
    return render(request, 'main/base_contact.html')


def entries(request):
    animal_entries = AnimalEntry.objects.all()
    return render(request, 'main/base_entries.html', context={'animals': animal_entries})

