from django.contrib import admin

# Register your models here.
from .models import Women, Category

admin.site.register(Women)
admin.site.register(Category)
