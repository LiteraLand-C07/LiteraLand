from django.shortcuts import render, redirect

# Create your views here.
from shared_models.models import Book
from .forms import BookRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def browse_books(request):
    books = Book.objects.all()  # Mengambil semua buku
    return render(request, 'browse_books.html', {'books': books})

# @login_required
def submit_book_request(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            book_request = form.save(commit=False)
            # nanti ganti aja kalo udah buat user, ini baru dummy
            # book_request.user = request.user
            dummy_user, created = User.objects.get_or_create(username='dummy_user')
            book_request.user = dummy_user
            book_request.save()
            return redirect('success_page')  # Redirect ke halaman sukses
    else:
        form = BookRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')