from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.db.models.aggregates import Count
from . import models

# Register your models here.

# @admin.register(models.Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['title', 'duedate', 'user']
#     list_editable = ['title']
#     list_per_page = 10

# @admin.register(models.User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'username']
#     full_name = ['first_name', 'last_name']
#     list_per_page = 10

    # @admin.display(ordering='products_count')
    # def products_count(self, collection):
    #     return collection.products_count
    
    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(products_count=Count('product'))