from django.contrib import admin
from .models.category import Category
from .models.post import BlogPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'reading_time', 'published_at']
    list_filter = ['status', 'category']
    search_fields = ['title', 'excerpt', 'content']
    ordering = ['-published_at', '-created_at']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'published_at'
