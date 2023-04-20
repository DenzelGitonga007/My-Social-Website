from django.contrib import admin

# Register your models here.
# Images app
from . models import Image
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created',]