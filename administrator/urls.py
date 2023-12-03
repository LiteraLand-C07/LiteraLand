from django.urls import path
from administrator.views import admin_page, add_queue, get_authors, get_genres, get_queues, add_books, delete_request, queues_json

app_name = 'administrator'

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('add-queue/', add_queue, name='add_queue'),
    path('get-authors/', get_authors, name='get_authors'),
    path('get-genres/', get_genres, name='get_genres'),
    path('get-queues/<str:author>/<str:genre>', get_queues, name='get_queues'),
    path('add-books/', add_books, name='add_books'),
    path('delete-request/<int:id>', delete_request, name='delete_request'),
    path('queues-json', queues_json, name='queues_json'),
]