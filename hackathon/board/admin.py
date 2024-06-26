from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'board_nickname', 'board_category', 'board_write_dttm', 'view_count')
    list_display_links = ('id', 'title')

admin.site.register(Board, BoardAdmin)
