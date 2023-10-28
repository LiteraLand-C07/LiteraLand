from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from administrator.models import BookQueue, Log
from administrator.forms import QueueForm
from shared_models.models import Book

# Create your views here.
def admin_page(request):
    log = Log.objects.all()
    form = QueueForm()

    context = {
        'log': log,
        'form': form,
    }
    return render(request, 'admin_page.html', context=context)

def add_queue(request):
    if request.method == "POST":
        form = QueueForm(request.POST)
        if form.is_valid():
            queue = form.save(commit=False)
            books = Book.objects.filter(ISBN=queue.ISBN)
            if len(books) != 0:
                return HttpResponseBadRequest("Book Already Exist")

            queue.user = request.user
            form.save()
            response = HttpResponse("Successfully added a book to queue")
            response.status_code = 200

            return response 
        
    return HttpResponseBadRequest("Form Not Valid")