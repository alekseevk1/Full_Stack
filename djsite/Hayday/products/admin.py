from django.contrib import admin

from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'price', 'amount', 'action', 'category', 'is_Ready')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_Ready', )
    list_filter = ('is_Ready', 'time_create')
    prepopulated_fields = {"slug" : ("title", )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {"slug" : ("name", )}

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
