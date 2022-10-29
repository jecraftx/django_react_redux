from django.contrib import admin
from my_app import models

admin.site.site_header = 'Панель 1'
admin.site.index_title = 'Панель 2'
admin.site.site_title = 'Панель 3'

class TextModelAdmin(admin.ModelAdmin):
    """Text Model"""

    list_display = (
        'author',
        'user',
        'created_datetime',
    )
    list_display_links = (
        'user',
        'created_datetime',
    )
    list_editable = (
        'text',
    )
    list_filter = (
        'author',
        'text',
        'created_datetime'
    )
    fieldsets = ((
            'Основное', {"fields": (
                'author',
                'text',
                'created_datetime',
            )}),
    )
    search_fields = [
        'author',
        'text',
        'created_datetime'
    ]

admin.site.reqister(models.TextModel, TextModelAdmin)
