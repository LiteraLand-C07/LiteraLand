from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shared_models.models import Book
from .models import BookReview
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login

from shared_models.models import Book
from .models import BookReview
from forumDiskusi.forms import BookReviewForm

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
# @login_required(login_url='/login')
def book_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = BookReview.objects.filter(book=book).values('username', 'review') # Getting usernames and reviews
    review_form = BookReviewForm()
    # print(123)
    # average_rating = BookReview.objects.filter(book=book).aggregate(rating=Avg)
    # if request.method == 'POST':
    #     body_unicode = request.body.decode('utf-8')
    #     body_data = json.loads(body_unicode)
    #     review_text = body_data.get('review')
    #     new_review = BookReview(book=book, review=review_text)
    #     new_review.save()
    #     return JsonResponse({'status': 'success'})
    context = {'book': book, 'reviews': reviews, 'review_form': review_form}
    # if request.method == 'GET':
    return render(request, 'diskusi.html', context)

def hello(request):
    return render(request,"hallo.html")

def delete_review(request, review_id):
    # Logika untuk menghapus review
    try:
        review = BookReview.objects.get(pk=review_id)
        if request.user.is_superuser:  # atau logika lainnya untuk mengecek admin
            review.delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Permission Denied'})
    except BookReview.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Review not found'})

@csrf_exempt
def ajax_add_review(request, pid):
    book = Book.objects.get(pk=pid)
    user = request.user
    review = BookReview.objects.create(
        book=book,
        user = user,
        review = request.POST['review'],
        star_rating = request.POST['star_rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'star_rating': request.POST['star_rating'],
    }

    return JsonResponse (
        {
            'bool':True,
         'context':context
         }
    )

