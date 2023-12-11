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

from shared_models.models import Book

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

def get_book_list_json(request):
    booklists = ListBook.objects.filter(access__icontains='public')
    return HttpResponse(serializers.serialize('json', booklists))

def get_my_book_lists(request):
    booklists = ListBook.objects.filter(user = request.user)
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
def create_booklist_flutter1(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_data = []

        for book in data["books"]:
            book_data.append(Book.objects.get(pk=book))

        new_product = ListBook.objects.create(
            user=request.user,
            name=data["name"],
            description=data["description"],
            image = "https://i.imgur.com/CFVTM7y.png",
            # Additional fields
            access=data["access"],
            books=book_data
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def get_booklists_json(request):
    booklists = ListBook.objects.filter(access__icontains='public')

    data = []
    for booklist in booklists:
        item = {
            'books': booklist.books,
            'name':booklist.name,
            'user': booklist.user,
            'access': booklist.access,
            'description': booklist.description,
        }
        data.append(item)
    return JsonResponse(data, safe=False)

@csrf_exempt
def create_booklist_flutter(request):
    if request.method == 'POST':
        try:
            # Assuming the Flutter app sends JSON data in the request body
            data = json.loads(request.body)

            # Extract data from JSON
            name = data.get('name')
            description = data.get('description')
            access = data.get('access')
            books = data.get('books')

            # Get the current user
            user = request.user
            print(name)

            # Create ListBook instance
            list_book = ListBook.objects.create(
                name=name,
                description=description,
                access=access,
                user=user,
                image='https://i.imgur.com/CFVTM7y.png'
            )

            # Add books to the list
            for book_id in books:
                try:
                    book = Book.objects.get(pk=book_id)
                    list_book.books.add(book)
                except Book.DoesNotExist:
                    # Handle the case when the book with the given ID does not exist
                    pass

            # Return response
            response_data = {
                'name': list_book.name,
                'description': list_book.description,
                'access': list_book.access,
                'books': list(list_book.books.values_list('id', flat=True)),
            }

            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)