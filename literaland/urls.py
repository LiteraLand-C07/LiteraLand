"""
URL configuration for literaland project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from browseBooks.views import browse_books
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('collections/',include('bookcollections.urls')),
    path('forumDiskusi/',include('forumDiskusi.urls')),
    path('authentication/',include('shared_models.urls')),
    path('administrator/', include('administrator.urls')),
    path('', include('browseBooks.urls')),
    # path('browse/', browse_books, name='browse_books'),
    # path('browse/', include('browseBooks.urls')),
    # path('', browse_books, name='home'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
