from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register


from persons.models import Person

@register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('name', 'first_name', 'last_name')
    icon_name = 'person'