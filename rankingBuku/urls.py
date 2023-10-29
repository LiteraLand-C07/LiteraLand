from django.urls import path
from rankingBuku.views import show_book_lists, create_book_list, get_book_lists_json, list_book_detail, get_book_list_byid, get_my_book_lists, delete_my_book_list, get_books

urlpatterns = [
    path('', show_book_lists, name='book_lists'),
    path('create_book_list/', create_book_list, name='create_book_list'),
    path('get-book-lists-json/', get_book_lists_json, name='get_book_lists_json'),
    path('list_book_detail/', list_book_detail, name='list_book_detail'),
    path('get_book_list_byid/', get_book_list_byid, name='get_book_list_byid'),
    path('get_my_book_lists/', get_my_book_lists, name='get_my_book_lists'),
    path('delete_my_book_list/', delete_my_book_list, name="delete_my_book_list"),
    path('get_books/', get_books, name='get_books'),
]