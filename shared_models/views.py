from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from shared_models.models import Book
from django.core import serializers


# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('shared_models:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Ambil URL dari parameter 'next' dalam permintaan
            """
            JANGAN LUPA UBAH DEFAULT PARAMETER KE BROWSE
            """
            next_url = request.GET.get('next','/')

            response = HttpResponseRedirect(next_url) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    """
    JANGAN LUPA GANTI KE BROWSE
    """
    response = HttpResponseRedirect(reverse('shared_models:login'))
    response.delete_cookie('last_login')
    return response

def book_json(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize("json", book), content_type = "application/json")