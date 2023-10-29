from django.shortcuts import render, redirect
from rankingBuku.models import ListBook
from rankingBuku.forms import ListBookForm
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from shared_models.models import Book

# Create your views here.
def show_book_lists(request):
    book_lists = ListBook.objects.all()
    context = {
        'book_lists': book_lists
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
            if 'image' in request.FILES:
                new_book_list.image = request.FILES['image']

            new_book_list.user = request.user

            if 'image' in request.FILES:
                new_book_list.image = request.FILES['image']
            
            new_book_list.save()
            new_book_list.books.set(form.cleaned_data['books'])

            # harusnya bisa direct ke page lain
            return HttpResponse(b"CREATED", status=201)
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

def list_book_detail(request):
    list_id = request.GET.get('id')  # Get the list ID from the query parameter
    listbook = ListBook.objects.get(pk=list_id)
    context = {
        'listbook': listbook,
        'books': listbook.books.all
        }
    return render(request, 'list_book_detail.html', context)

@login_required(login_url='/authentication/login')
def delete_my_book_list(request):
    if request.method == 'DELETE':
        list_id = request.GET.get('id')
        my_book_list = get_object_or_404(ListBook, pk=list_id)

        # Check if the user has permission to delete the book list
        if request.user == my_book_list.user:
            my_book_list.delete()
            return JsonResponse({'message': 'Book list deleted successfully.'}, status=200)
        else:
            return JsonResponse({'error': 'Permission denied.'}, status=403)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    
def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        deleteBooklist =  ListBook.objects.get(id=item_id)
        deleteBooklist.delete()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})