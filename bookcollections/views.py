import json
from django.shortcuts import render
from shared_models.models import Book
from bookcollections.models import BookCollection, StatusBaca
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .forms import SearchForm,BookCollectionForm
from django.contrib.auth.models import User

# Create your views here.
def show_detail_buku(request,id):
    book = Book.objects.get(pk=id)
    average_rating = BookCollection.objects.filter(book=book, rating__gt=0).aggregate(Avg('rating'))['rating__avg']
    form = BookCollectionForm()

    context = {
        'book':book,
        'rating':average_rating,
        'StatusBaca':StatusBaca,
        'range':range(1,11),
        'user':request.user,
        'form':form,
    }

    return render(request,'detail_buku.html',context)

def get_detail_json(request,id):
    book = Book.objects.get(pk=id)
    average_rating = BookCollection.objects.filter(book=book, rating__gt=0).aggregate(Avg('rating'))['rating__avg']
    item = {
        'rating' : average_rating,
        'title' : book.title,
        'author' : book.author,
        'publisher': book.publisher,
        'page_count' : book.page_count,
        'genre':book.genre,
        'ISBN': book.ISBN,
        'language':book.language,
        'published_date' : book.published_date,
        'description':book.description,
    }
    data = []
    data.append(item)

    return JsonResponse(data, safe=False)

def get_collection_json(request,id):
    book = Book.objects.get(pk=id)
    book_collection = BookCollection.objects.filter(book=book,user=request.user)
    return HttpResponse(serializers.serialize('json', book_collection))

@csrf_exempt
def add_collection(request,id):
    form = BookCollectionForm(request.POST)

    if form.is_valid() and request.method == 'POST':
        book_data = Book.objects.get(pk=id)
        new_collection = form.save(commit=False)
        new_collection.user = request.user
        new_collection.book = book_data

        new_collection.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def edit_collection(request,id):
    bookCollection = BookCollection.objects.get(pk=id)

    if request.method == 'POST':
        form = BookCollectionForm(request.POST, instance=bookCollection)
        if form.is_valid():
            edited_item = form.save(commit=False)
            edited_item.save()

            return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound() 

@login_required(login_url='/authentication/login')
def show_collections(request):
    book_collections = BookCollection.objects.filter(user=request.user)
    form = SearchForm()
    
    context = {
        'book_collections':book_collections,
        'StatusBaca':StatusBaca,
        'user':request.user.username,
        'form':form,
    }

    return render(request,'collections.html',context)

def get_collections_json(request):
    collections = BookCollection.objects.filter(user=request.user)

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_type = form.cleaned_data['search_type']
            if search_type == 'title':
                collections = collections.filter(book__title__icontains=query)
            elif search_type == 'genre':
                collections = collections.filter(book__genre__icontains=query)
            elif search_type == 'author':
                collections = collections.filter(book__author__icontains=query)


    data = []
    for collection in collections:
        item = {
            'book': collection.book.pk,
            'title':collection.book.title,
            'author':collection.book.author,
            'page_count': collection.book.page_count,
            'genre': collection.book.genre,
            'ISBN': collection.book.ISBN,
            'pk' : collection.pk,
            'rating': collection.rating,
            'current_page': collection.current_page,
            'status_baca': collection.status_baca,
            'status_baca_display': collection.get_status_baca_display(),
        }
        data.append(item)
    return JsonResponse(data, safe=False)


@csrf_exempt
def add_current_page(request,id):
    collection = BookCollection.objects.get(pk=id)
    book_page = collection.book.page_count
    
    if request.method == 'POST':
        collection.current_page += 1
        if collection.current_page > book_page:
            collection.current_page = book_page

        collection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def add_ten_current_page(request,id):
    collection = BookCollection.objects.get(pk=id)
    book_page = collection.book.page_count
    
    if request.method == 'POST':
        collection.current_page += 10
        if collection.current_page > book_page:
            collection.current_page = book_page

        collection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def decrease_current_page(request,id):
    collection = BookCollection.objects.get(pk=id)
    
    if request.method == 'POST':
        collection.current_page -= 1
        if collection.current_page < 0:
            collection.current_page = 0
        collection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def decrease_ten_current_page(request,id):
    collection = BookCollection.objects.get(pk=id)
    
    if request.method == 'POST':
        collection.current_page -= 10
        if collection.current_page < 0 :
            collection.current_page = 0
        collection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def edit_rating_collection(request,id,new_rating):
    if request.method == 'POST':
        bookCollection = BookCollection.objects.get(pk=id)
        
        bookCollection.rating = new_rating
        bookCollection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound() 

@csrf_exempt
def edit_status_collection(request,id,new_status):
    if request.method == 'POST':
        bookCollection = BookCollection.objects.get(pk=id)
        
        bookCollection.status_baca = new_status
        bookCollection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound() 

@csrf_exempt
def delete_collection(request,id):
    if request.method == 'DELETE':
        collection = BookCollection.objects.get(pk=id)
        collection.delete()

        return HttpResponse(b"DELETED",status=201)
    
    return HttpResponseNotFound()

def read_book_content(request,id):
    book = Book.objects.get(pk=id)

    context = {
        'book': book,
    }

    return render(request,'read_book.html',context)

@csrf_exempt
def create_collection_flutter(request,id):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        book_data = Book.objects.get(pk=id)

        new_product = BookCollection.objects.create(
            user = request.user,
            book = book_data,
            rating = data["rating"],
            current_page = int(data["current_page"]),
            status_baca = data["status_baca"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def edit_collection_flutter(request,id):
    if request.method == 'POST':

        data = json.loads(request.body)
        bookCollection = BookCollection.objects.get(pk=id)

        new_rating = data["rating"],
        new_current_page = int(data["current_page"]),
        new_status_baca = data["status_baca"]

        bookCollection.rating = new_rating
        bookCollection.current_page = new_current_page
        bookCollection.status_baca = new_status_baca

        bookCollection.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
