import json
from django.shortcuts import render, redirect
from rankingBuku.models import ListBook
from rankingBuku.forms import ListBookForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_book_lists(request):
    book_lists = ListBook.objects.all()
    context = {
        'book_lists': book_lists,
    }
    return render(request, 'rankingBuku.html', context)

@login_required(login_url='/authentication/login')
@csrf_exempt
def create_book_list(request):
    if request.method == 'POST':
        form = ListBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Get or create the user
            new_book_list = form.save(commit=False)
            new_book_list.user = request.user

            if 'image' in request.FILES:
                new_book_list.image = request.FILES['image']
            
            new_book_list.save()
            new_book_list.books.set(form.cleaned_data['books'])

            return HttpResponseRedirect(reverse('book_lists'))
    else:
        form = ListBookForm()

    context = {'form': form}
    return render(request, 'create_book_list.html', context)

def get_book_lists_json(request):
    booklists = ListBook.objects.filter(access__icontains='public')
    return HttpResponse(serializers.serialize('json', booklists))

@login_required(login_url='/authentication/login')
def get_my_book_lists(request):
    booklists = ListBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', booklists))

def get_book_list_byid(request):
    booklist = ListBook.objects.get(pk=request.GET.get('id'))
    return HttpResponse(serializers.serialize('json', booklist))

def get_books(request):
    booklist = ListBook.objects.get(pk=request.GET.get('id'))
    books = booklist.books.all()
    return HttpResponse(serializers.serialize('json', books))

def list_book_detail(request, id):
    # list_id = request.GET.get('id')  # Get the list ID from the query parameter
    listbook = ListBook.objects.get(pk=id)
    context = {
        'listbook': listbook,
        'books': listbook.books.all
        }
    return render(request, 'list_book_detail.html', context)

@login_required(login_url='/authentication/login')
def delete_listbook(request, id):
    listbook = ListBook.objects.get(pk =id)
    listbook.delete()
    return HttpResponseRedirect(reverse('book_lists'))

@csrf_exempt
@login_required(login_url='/authentication/login')
def create_listbook_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_product = ListBook.objects.create(
            user=request.user,
            name=data["fields"]["name"],
            user=data["fields"]["user"],
            description=data["fields"]["description"],
            image=data["fields"]["image"],
            # Additional fields
            access=data["fields"]["access"],
            books=data["fields"]["books"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)