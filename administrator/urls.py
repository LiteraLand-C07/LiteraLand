from django.urls import path
from administrator.views import admin_page, add_queue

app_name = 'administrator'

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('add-queue', add_queue, name='add_queue'),
]