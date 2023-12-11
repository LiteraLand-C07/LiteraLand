from django.urls import path
from administrator.views import admin_page, add_queue, get_authors, get_genres, get_queues, add_books, delete_request, queues_json, create_queue_flutter
from administrator.views import delete_queue_flutter, request_json, delete_request_flutter, confirm_queue

app_name = 'administrator'

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('add-queue/', add_queue, name='add_queue'),
    path('get-authors/', get_authors, name='get_authors'),
    path('get-genres/', get_genres, name='get_genres'),
    path('get-queues/<str:author>/<str:genre>', get_queues, name='get_queues'),
    path('add-books/', add_books, name='add_books'),
    path('delete-request/<int:id>', delete_request, name='delete_request'),
    path('queues-json/', queues_json, name='queues_json'),
    path('create-flutter/', create_queue_flutter , name='create_queue_flutter'),
    path('request-json', request_json, name='request_json'),
    path('delete-queue-flutter/<int:id>', delete_queue_flutter, name='delete_queue_flutter'),
    path('delete-request-flutter/<int:id>', delete_request_flutter, name='delete_request_flutter'),
    path('confirm-queue', confirm_queue, name='confirm_queue'),
]