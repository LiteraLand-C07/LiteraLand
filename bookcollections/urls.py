from django.urls import path
from bookcollections.views import show_detail_buku

app_name = 'bookcollections'

urlpatterns = [
    path('detail_buku/<int:id>/',show_detail_buku,name="show_detail_buku")
]