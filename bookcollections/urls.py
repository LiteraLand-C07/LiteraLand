from django.urls import path
from bookcollections.views import show_detail_buku,add_collection,get_collection_json,edit_collection,show_collections

app_name = 'bookcollections'

urlpatterns = [
    path('detail_buku/<int:id>/',show_detail_buku,name="show_detail_buku"),
    path('add_collection/<int:id>/',add_collection,name="add_collection"),
    path('get_collection_json/<int:id>/',get_collection_json,name="get_collection_json"),
    path('edit_collection/<int:id>/',edit_collection,name="edit_collection"),
    path('',show_collections,name="show_collections")
]