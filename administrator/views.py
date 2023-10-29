from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from administrator.models import BookQueue, Log
from administrator.forms import QueueForm
from shared_models.models import Book
from browseBooks.models import BookRequest
import json
from django.views.decorators.http import require_http_methods
from django.core import serializers

# Create your views here.
def admin_page(request):
    log = Log.objects.all()
    form = QueueForm()
    book_request = BookRequest.objects.all().order_by("-pk")

    context = {
        'log': log,
        'form': form,
        'reqs': book_request,
    }
    return render(request, 'admin_page.html', context=context)

@require_http_methods(["POST"])
def add_queue(request):
    form = QueueForm(request.POST)
    if form.is_valid():
        queue = form.save(commit=False)
        books = Book.objects.filter(ISBN=queue.ISBN)
        allQueue = BookQueue.objects.filter(ISBN=queue.ISBN)

        if len(books) != 0 or len(allQueue) != 0:
            return HttpResponseBadRequest("Book Already Exist")

        queue.user = request.user
        form.save()
        response = HttpResponse("Successfully added a book to queue")
        response.status_code = 200

        return response 
        
    return HttpResponseBadRequest("Form Not Valid")

@require_http_methods(["GET"])
def get_authors(request):
    queue = BookQueue.objects.filter(user=request.user)
    authors = list(set(book.author for book in queue))
    return HttpResponse(json.dumps(authors))

@require_http_methods(["GET"])
def get_genres(request):
    queue = BookQueue.objects.all()
    raw_genres = set(book.genre for book in queue)
    genres = set()
    for raw_genre in raw_genres:
        for temp_genre in raw_genre.split(","):
            genres.add(temp_genre.strip())

    genres = list(genres)
    return HttpResponse(json.dumps(genres))

@require_http_methods(["GET"])
def get_queues(request, author, genre):
    queues = BookQueue.objects.all()
    if author != "Author":
        temp = queues
        for queue in temp:
            if author != queue.author:
                queues = queues.exclude(id=queue.id)

    if genre != "Genre":
        temp = queues
        for queue in temp:
            splitted = queue.genre.split(",")
            if genre not in [temp.strip() for temp in splitted]:
                queues = queues.exclude(id=queue.id)

    return HttpResponse(serializers.serialize('json', queues))

@require_http_methods(["POST"])
def add_books(request):
    queues = BookQueue.objects.filter(user=request.user)
    author = request.POST.get('AuthorFilter') 
    genre = request.POST.get('GenreFilter') 

    if author != "Author":
        temp = queues
        for queue in temp:
            if author != queue.author:
                queues = queues.exclude(id=queue.id)

    if genre != "Genre":
        temp = queues
        for queue in temp:
            splitted = queue.genre.split(",")
            if genre not in [temp.strip() for temp in splitted]:
                queues = queues.exclude(id=queue.id)

    is_adding = False
    for queue in queues:
        books = Book.objects.filter(ISBN=queue.ISBN)
        if len(books) == 0:
            new_book = Book(title=queue.title, author=queue.author, description=queue.description, publisher=queue.publisher, page_count=queue.page_count, genre=queue.genre, ISBN=queue.ISBN, language=queue.language, published_date=queue.published_date)
            new_book.save()
            is_adding = True
        queue.delete()

    if is_adding:
        return HttpResponse("Successfully Added New Books")
    return HttpResponseBadRequest("Failed To Add New Books")
