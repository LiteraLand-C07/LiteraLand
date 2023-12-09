import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shared_models.models import Book
from .models import BookReview
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shared_models.models import Book
from .models import BookReview
from forumDiskusi.forms import BookReviewForm

from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required
def book_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    star_filter = request.GET.get('star_filter', None)

    if star_filter == 'lte3':
        reviews = BookReview.objects.filter(book=book, star_rating__lte=3).select_related('user')
    elif star_filter == 'gt3':
        reviews = BookReview.objects.filter(book=book, star_rating__gt=3).select_related('user')
    else:
        reviews = BookReview.objects.filter(book=book).select_related('user')

    review_form = BookReviewForm()
    context = {'book': book, 'reviews': reviews, 'review_form': review_form, 'current_user': request.user}
    return render(request, 'diskusi.html', context)

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

# Endpoint baru untuk mengambil semua review dalam format JSON
def show_json(request):
    data = BookReview.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = BookReview.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = BookReview.objects.create(
            user = request.user,
            book = request.book,
            reviewer_name = data["reviewer_name"],
            star_rating = int(data["star_rating"]),
            review = data["review"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)