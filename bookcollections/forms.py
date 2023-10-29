from django import forms
from django.forms import ModelForm
from .models import BookCollection


class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('title', 'Judul'),
        ('genre', 'Genre'),
        ('author', 'Penulis'),
    ]

    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cari buku...'}))
    search_type = forms.ChoiceField(choices=SEARCH_CHOICES)

class BookCollectionForm(ModelForm):
    class Meta:
        model = BookCollection
        fields = ["rating","current_page","status_baca"]
    
