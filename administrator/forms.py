from django.forms import ModelForm
from administrator.models import BookQueue

class QueueForm(ModelForm):
    class Meta:
        model = BookQueue
        fields = ["title", "author", "publisher", "page_count", "genre", "ISBN", "language", "published_date","description"]