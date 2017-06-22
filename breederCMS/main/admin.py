from django.contrib import admin
from django.db import models
from .models import AnimalEntry
from daguerre.widgets import AreaWidget


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': AreaWidget},
    }


admin.site.register(AnimalEntry, MyModelAdmin)

