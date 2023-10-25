from django.shortcuts import render
from shared_models.models import Book
from bookcollections.models import BookCollection, StatusBaca
from django.http import HttpResponseRedirect,HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
import json

# Create your views here.
def show_detail_buku(request,id):
    book = Book.objects.get(pk=id)
    average_rating = BookCollection.objects.filter(book=book, rating__gt=0).aggregate(Avg('rating'))['rating__avg']

    context = {
        'book':book,
        'rating':average_rating,
        'StatusBaca':StatusBaca,
        'range':range(1,11),
    }

    return render(request,'detail_buku.html',context)

def get_collection_json(request,id):
    book = Book.objects.get(pk=id)
    # JANGAN LUPA FILTER TERHADAP USER JUGA
    book_collection = BookCollection.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', book_collection))

@csrf_exempt
def add_collection(request,id):
    if request.method == 'POST':
        book_data = Book.objects.get(pk=id)
        rating = request.POST.get('rating')
        current_page = request.POST.get('current_page')
        status_baca = request.POST.get('status_baca')

        new_collection = BookCollection(book=book_data,rating=rating,current_page=current_page,status_baca=status_baca)
        new_collection.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def edit_collection(request,id):
    if request.method == 'POST':
        bookCollection = BookCollection.objects.get(pk=id)
        rating = request.POST.get('rating')
        current_page = request.POST.get('current_page')
        status_baca = request.POST.get('status_baca')

        bookCollection.rating = rating
        bookCollection.current_page = current_page
        bookCollection.status_baca = status_baca
        bookCollection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound() 

def show_collections(request):
    # JANGAN LUPA FILTER TERHADAP USER
    book_collections = BookCollection.objects.all()
    context = {
        'book_collections':book_collections,
        'StatusBaca':StatusBaca,
    }

    return render(request,'collections.html',context)

def get_collections_json(request):
    collections = BookCollection.objects.all()
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
            'status_baca_display': collection.get_status_baca_display(),  # add this line
            # add other fields if necessary
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