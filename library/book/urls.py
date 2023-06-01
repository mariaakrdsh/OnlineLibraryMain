from django.urls import path, include

from .views import books, book_item, books_list, delete_book
from . import views

from book.views import BookViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework import routers

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')


urlpatterns = [
    path('', books),
    path('api/', include(router.urls)),
    path('', books, name='books'),
    path('books', books),
    path('books_list', books_list, name='books_list'),
    path('books/<int:book_id>/', book_item, name='book_item'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
    path('books/add_book/<int:book_id>/', views.add_book, name='add_book'),

]
