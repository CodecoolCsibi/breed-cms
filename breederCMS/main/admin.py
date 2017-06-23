from django.contrib import admin
from pyuploadcare.dj.forms import FileWidget

from .models import AnimalEntry
from django.forms import ModelForm


class AnimalForm(ModelForm):
    class Meta:
        model = AnimalEntry
        fields = ['name', 'gender', 'status', 'color', 'date_of_birth', 'picture', 'description']
        widgets = {
            'picture': FileWidget(attrs={
                'data-cdn-base': 'https://cdn.super-candidates.com',
                'data - crop': '300x300 minimum',
                'data-images-only': 'true',
                'data-tabs': 'file facebook camera gdrive',
                'data-image-shrink': '1024x1024'
            })
        }


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'status', 'color')
    search_fields = ['name', 'description']
    form = AnimalForm


admin.site.register(AnimalEntry, AnimalAdmin)
