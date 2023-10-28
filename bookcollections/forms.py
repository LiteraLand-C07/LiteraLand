from django import forms

class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('title', 'Judul'),
        ('genre', 'Genre'),
        ('author', 'Penulis'),
    ]

    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cari buku...'}))
    search_type = forms.ChoiceField(choices=SEARCH_CHOICES)
