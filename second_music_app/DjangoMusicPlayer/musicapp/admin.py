from django.contrib import admin
from .models import Song
# Register your models here.
@admin.register(Song)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'pk','audio_link','title','artist'
    list_display_links = 'pk','audio_link','title','artist'