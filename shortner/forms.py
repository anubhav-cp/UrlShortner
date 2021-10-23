from django.db.models import fields
from django.forms import ModelForm
from .models import URL

class UrlShortner(ModelForm):
    class Meta:
        model = URL
        fields = ['full_url']
        labels = {
            "full_url": ""
        }

    def __init__(self, *args, **kwargs):
        super(UrlShortner, self).__init__(*args, **kwargs)
        self.fields['full_url'].widget.attrs.update({'class': 'myfieldclass', 'placeholder': 'Enter the link here', 'label': ''})