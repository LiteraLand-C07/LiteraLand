from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from administrator.models import BookQueue, Log
from administrator.forms import QueueForm

# Create your views here.
def admin_page(request):
    book_queue = BookQueue.objects.all()
    log = Log.objects.all()
    form = QueueForm()

    context = {
        'queue': book_queue,
        'log': log,
        'form': form,
    }
    return render(request, 'admin_page.html', context=context)