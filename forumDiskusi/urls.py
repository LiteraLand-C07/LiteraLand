from django.urls import path
from forumDiskusi.views import book_reviews, hello, delete_review
from bookcollections.views import show_detail_buku

app_name = 'forumDiskusi'

urlpatterns = [
    path('', hello, name="hello"),
    path('detail_buku/<int:id>/', show_detail_buku, name="show_detail_buku"),
    path('book_reviews/<int:book_id>/', book_reviews, name='book_reviews'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
]