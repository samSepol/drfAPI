from django.contrib import admin
from .models import Coder
# Register your models here.

@admin.register(Coder)
class CoderAdmin(admin.ModelAdmin):
    list_display=['id','name','domain','company','salary']

    list_filter=['id','domain','company']

