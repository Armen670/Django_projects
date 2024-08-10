from django.contrib import admin
from .models import Room, Post, News

# Register your models here.

admin.site.register(Room)
admin.site.register(Post)
admin.site.register(News)