from django.contrib import admin
from .models import AnimalEntry
from django.forms import ModelForm


class AnimalForm(ModelForm):
    class Meta:
        model = AnimalEntry
        fields = ['name', 'gender', 'status', 'color', 'date_of_birth', 'picture', 'description']


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'status', 'color')
    search_fields = ['name', 'description']
    form = AnimalForm

admin.site.register(AnimalEntry, AnimalAdmin)





