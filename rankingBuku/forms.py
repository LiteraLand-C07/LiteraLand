from django import forms
from rankingBuku.models import ListBook
from shared_models.models import Book

class ListBookForm(forms.ModelForm):
    image = forms.ImageField(required=True, label='Cover Image')
    
    class Meta:
        model = ListBook
        fields = ['name', 'access', 'description', 'books', 'image']
        widgets = {
            'books': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(ListBookForm, self).__init__(*args, **kwargs)
        # Define the queryset for the 'books' field here.
        self.fields['books'].queryset = Book.objects.all()
