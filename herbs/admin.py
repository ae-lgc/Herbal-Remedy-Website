from django.contrib import admin
from .models import Herb

@admin.register(Herb)
class HerbAdmin(admin.ModelAdmin):
    list_display = ('local_name', 'english_name', 'scientific_name')

