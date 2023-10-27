from django.urls import path
from rankingBuku.views import show_book_lists, create_book_list, get_book_lists_json

urlpatterns = [
    path('', show_book_lists, name='book_lists'),
    path('create_book_list/', create_book_list, name='create_book_list'),
    path('get-book-lists-json/', get_book_lists_json, name='get_book_lists_json'),
]
