from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Category)
class CategoryAdmin(admin.ModelAdmin): # ai class ar objective holo slug field ar requirement full fill kora.
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(models.Category, CategoryAdmin) 