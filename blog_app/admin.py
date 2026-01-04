from django.contrib import admin
from .models import Category, Blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)
admin.site.register(Category, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'Category', 'status', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('status', 'is_featured', 'created_at', 'Category')
    search_fields = ('title', 'author__username', 'Category__category_name') # author__username to search by author's username, Category__category_name to search by category name due to foreign key we use __
    prepopulated_fields = {'slug': ('title',)}  # auto fill slug field based on title
    
admin.site.register(Blog, BlogAdmin)