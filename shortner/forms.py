from django.db.models import fields
from django.forms import ModelForm
from .models import URL

class UrlShortner(ModelForm):
    class Meta:
        model = URL
        fields = ['full_url']