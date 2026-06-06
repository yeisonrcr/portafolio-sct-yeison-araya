from django.contrib import admin
from .models.case_study import CaseStudy


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'industry', 'company_size', 'is_published', 'order']
    list_filter = ['is_published', 'industry']
    search_fields = ['title', 'problem', 'solution', 'result']
    ordering = ['order', '-created_at']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at']
    fieldsets = (
        ('Información', {
            'fields': ('title', 'slug', 'industry', 'company_size', 'is_published', 'order')
        }),
        ('Contenido', {
            'fields': ('problem', 'solution', 'result')
        }),
        ('Métricas destacadas', {
            'fields': (
                ('metric_1_label', 'metric_1_value'),
                ('metric_2_label', 'metric_2_value'),
                ('metric_3_label', 'metric_3_value'),
            )
        }),
    )
