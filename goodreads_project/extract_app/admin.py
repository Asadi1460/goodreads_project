from django.contrib import admin
from django.contrib.admin import register

from .models import Book


# Register your models here.
@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'published_year')
    search_fields = ('title', 'author', 'publish_date')
    list_display_links = ('title', 'author')
