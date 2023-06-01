from django.contrib import admin

from order.models import Order, Book
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ("surname", "name",)

    def book(self, obj):
        return [f"{book.name}" for book in obj.books.all()]

    def books(self, obj):
        return [book for book in obj.books.all()]

    list_display = ('id', 'name', 'surname', 'patronymic', "book")
    list_display_links = ('id', 'name', 'surname', 'patronymic', "book")

    list_filter = ('name', 'id', 'surname', 'patronymic', "books")
    search_fields = ('name', 'surname', 'patronymic',)
    search_help_text = "search_fields = name, surname, patronymic"
