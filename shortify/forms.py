from django import forms

from .models import ShortifyURL


class ShortifyCreateForm(forms.ModelForm):
    url = forms.URLField(label="URL to shorten")

    class Meta:
        model = ShortifyURL
        fields = ["url"]
