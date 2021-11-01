from django import forms
from django.core.exceptions import ValidationError

widget_textinput = forms.TextInput(
    attrs={
        "type": "number",
        "class": "form-control"
    }
)


class TextForm(forms.Form):
    number = forms.CharField(max_length=255,widget=widget_textinput)
