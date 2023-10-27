from django.urls import path
from administrator.views import admin_page

app_name = 'administrator'

urlpatterns = [
    path('', admin_page, name='admin_page'),
]