
from django import forms
from .models import Short
import re


class ShortForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = ['long_url']
    long_url = forms.CharField(label='LONG URL', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text', 'required': 'required', 'placeholder': 'LONG URL'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        long_url = cleaned_data.get("long_url")
        url_regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not re.match(long_url, url_regex):
            raise forms.ValidationError("Invalid URL")
