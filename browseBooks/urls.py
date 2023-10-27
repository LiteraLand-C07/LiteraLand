from django.urls import path
from .views import browse_books
from .views import submit_book_request
from .views import success_page

urlpatterns = [
    path('browse/', browse_books, name='browse_books'),
    path('submit-request/', submit_book_request, name='submit_book_request'),
    path('success/', success_page, name='success_page'),
    
]

