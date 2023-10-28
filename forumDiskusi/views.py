from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shared_models.models import Book
from .models import BookReview
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared_models.models import Book
from .models import BookReview
from forumDiskusi.forms import BookReviewForm

from django.contrib.auth.decorators import login_required

@login_required
def book_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = BookReview.objects.filter(book=book_id).select_related('user') # Getting usernames and reviews
    review_form = BookReviewForm()
    context = {'book': book, 'reviews': reviews, 'review_form': review_form, 'current_user': request.user}
    return render(request, 'diskusi.html', context)

def hello(request):
    return render(request,"hallo.html")

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

def delete_review(request, book_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'fail', 'message': 'User not authenticated'})

        review_id = request.POST.get('review_id')
        try:
            review = BookReview.objects.get(pk=review_id)
            if review.user == request.user or request.user.is_superuser:  # check if the user is the owner or admin
                review.delete()
                return JsonResponse({'status': 'success', 'message': 'Review deleted successfully'})
            else:
                return JsonResponse({'status': 'fail', 'message': 'Permission denied'})
        except BookReview.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Review does not exist'})