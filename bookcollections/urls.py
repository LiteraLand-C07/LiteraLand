from django.urls import path
from bookcollections.views import show_detail_buku,add_collection,get_collection_json,edit_collection,show_collections,add_current_page,add_ten_current_page,decrease_current_page,decrease_ten_current_page,edit_rating_collection,edit_status_collection,get_collections_json,delete_collection,read_book_content,get_json,get_json_by_user,create_collection_flutter,edit_collection_flutter

app_name = 'bookcollections'

urlpatterns = [
    path('detail_buku/<int:id>/',show_detail_buku,name="show_detail_buku"),
    path('add_collection/<int:id>/',add_collection,name="add_collection"),
    path('get_collection_json/<int:id>/',get_collection_json,name="get_collection_json"),
    path('edit_collection/<int:id>/',edit_collection,name="edit_collection"),
    path('',show_collections,name="show_collections"),
    path('get_collections_json/',get_collections_json,name="get_collections_json"),
    path('add_current_page/<int:id>/',add_current_page,name="add_current_page"),
    path('add_ten_current_page/<int:id>/',add_ten_current_page,name="add_ten_current_page"),
    path('decrease_current_page/<int:id>/',decrease_current_page,name="decrease_current_page"),
    path('decrease_ten_current_page/<int:id>/',decrease_ten_current_page,name="decrease_ten_current_page"),
    path('edit_rating_collection/<int:id>/<int:new_rating>/',edit_rating_collection,name="edit_rating_collection"),
    path('edit_status_collection/<int:id>/<str:new_status>/',edit_status_collection,name="edit_status_collection"),
    path('delete_collection/<int:id>/',delete_collection,name="delete_collection"),
    path('read_book_content/<int:id>/',read_book_content,name="read_book_content"),
    path('json/',get_json,name="get_json"),
    path('json/<str:username>/',get_json_by_user,name="get_json_by_user"),
    path('create_flutter/<int:id>/',create_collection_flutter,name="create_collection_flutter"),
    path('edit_flutter/<int:id>',edit_collection_flutter,name="edit_collection_flutter"),
]