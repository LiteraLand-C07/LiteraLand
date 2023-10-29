from django.urls import path
from .views import browse_books
from .views import submit_book_request
from .views import success_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', browse_books, name='browse_books'),
    path('submit-request/', submit_book_request, name='submit_book_request'),
    path('success/', success_page, name='success_page'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/authentication/login'), name='logout'),
]