from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shared_models.models import Book
from .models import BookReview
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json

from shared_models.models import Book
from .models import BookReview
# @login_required
def book_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = BookReview.objects.filter(book=book).values('user__username', 'review')  # Getting usernames and reviews
    context = {'book': book, 'reviews': reviews}
    print(123)
    
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        review_text = body_data.get('review')
        new_review = BookReview(user=request.user, book=book, review=review_text)
        new_review.save()
        return JsonResponse({'status': 'success'})
    
    if request.method == 'GET':
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