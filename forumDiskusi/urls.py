from django.urls import path
from forumDiskusi.views import book_reviews, hello,ajax_add_review, delete_review
from bookcollections.views import show_detail_buku
from browseBooks.views import browse_books


app_name = 'forumDiskusi'

urlpatterns = [
    path('', hello, name="hello"),
    path('detail_buku/<int:id>/', show_detail_buku, name="show_detail_buku"),
    path('book_reviews/<int:book_id>/', book_reviews, name='book_reviews'),
    path('delete_review/<int:book_id>/', delete_review, name='delete_review'),
    path('ajax_add_review/<int:pid>/',ajax_add_review, name='ajax_add_review'),
    path('browse_books/', browse_books, name='browse_books'),
]
