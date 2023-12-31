from django.urls import path
from rankingBuku.views import show_book_lists, create_book_list, get_book_list_json, list_book_detail, get_book_list_byid, get_my_book_lists, delete_listbook, get_books, create_booklist_flutter, get_booklists_json, delete_flutter

urlpatterns = [
    path('', show_book_lists, name='book_lists'),
    path('create_book_list/', create_book_list, name='create_book_list'),
    path('get-book-list-json/', get_book_list_json, name='get_book_list_json'),
    path('list_book_detail/<int:id>', list_book_detail, name='list_book_detail'),
    path('get_book_list_byid/', get_book_list_byid, name='get_book_list_byid'),
    path('get_my_book_lists/', get_my_book_lists, name='get_my_book_lists'),
    path('delete_listbook/<int:id>', delete_listbook, name="delete_listbook"),
    path('get_books/', get_books, name='get_books'),
    path('create_booklist_flutter/', create_booklist_flutter, name='create_booklist_flutter'),
    path('get-book-lists-json/', get_booklists_json, name='get_book_lists_json'),
    path('delete-booklist-flutter/<int:id>/', delete_flutter, name='delete-booklist-flutter'),
]