from django import forms
from forumDiskusi.models import BookReview

class BookReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Write Review"}))

    class Meta :
        model = BookReview
        fields = ['review','star_rating']