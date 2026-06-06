from django.contrib import admin
from django.utils.html import format_html
from .models.project import Project
from .models.project_image import ProjectImage
from .models.technology import Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'color', 'order']
    search_fields = ['name']
    ordering = ['order', 'name']
    prepopulated_fields = {'slug': ('name',)}


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'caption', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'is_featured', 'status',
        'users_count', 'carousel_order', 'updated_at'
    ]
    list_filter = ['status', 'is_featured', 'technologies']
    search_fields = ['title', 'description']
    ordering = ['-is_featured', 'carousel_order']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['technologies']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProjectImageInline]
    fieldsets = (
        ('Información principal', {
            'fields': ('title', 'slug', 'subtitle', 'short_description', 'description')
        }),
        ('Visual', {
            'fields': ('cover_image', 'technologies')
        }),
        ('Configuración', {
            'fields': ('is_featured', 'status', 'carousel_order')
        }),
        ('Métricas', {
            'fields': ('users_count', 'duration_months')
        }),
        ('Links', {
            'fields': ('url_live', 'url_repo')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
