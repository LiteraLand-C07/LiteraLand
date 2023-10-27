from django.shortcuts import render, redirect
from rankingBuku.models import ListBook
from rankingBuku.forms import ListBookForm
from django.http import HttpResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
def show_book_lists(request):
    book_lists = ListBook.objects.all()
    context = {
        'book_lists': book_lists
    }
    return render(request, 'rankingBuku.html', context)

@csrf_exempt
def create_book_list(request):
    if request.method == 'POST':
        form = ListBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Get or create the user
            user, created = User.objects.get_or_create(username="sasasasa")

            # Save the ListBook instance, but commit=False to set the user field first
            new_book_list = form.save(commit=False)
            new_book_list.user = user

            if 'image' in request.FILES:
                new_book_list.image = request.FILES['image']

            new_book_list.save()

            # Now, add the selected books to the new BookList instance
            new_book_list.books.set(form.cleaned_data['books'])

            return HttpResponse(b"CREATED", status=201)
    else:
        form = ListBookForm()

    context = {'form': form}
    return render(request, 'create_book_list.html', context)

def get_book_lists_json(request):
    booklists = ListBook.objects.filter(access__icontains='public')
    return HttpResponse(serializers.serialize('json', booklists))
