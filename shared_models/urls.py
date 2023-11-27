from shared_models.views import register,login_user,logout_user, book_json
from django.urls import path

app_name = 'shared_models'

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout"),
    path('json/', book_json, name="book_json"),
]