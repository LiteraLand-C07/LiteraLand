from django.urls import path
from forumDiskusi.views import book_reviews, ajax_add_review, delete_review, show_json, show_json_by_id, create_product_flutter, book_reviews_id
from bookcollections.views import show_detail_buku
from browseBooks.views import browse_books
from django.contrib.auth.decorators import login_required


app_name = 'forumDiskusi'

urlpatterns = [
    path('detail_buku/<int:id>/', show_detail_buku, name="show_detail_buku"),
    path('book_reviews/<int:book_id>/', book_reviews, name='book_reviews'),
    path('delete_review/<int:book_id>/', delete_review, name='delete_review'),
    path('ajax_add_review/<int:pid>/',ajax_add_review, name='ajax_add_review'),
    path('browse_books/', browse_books, name='browse_books'),
    path('show_json/', show_json, name='show_json'),
    path('json_id/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('book-reviews_id/<int:book_id>/', login_required(book_reviews_id), name='book_reviews_id'),
]
