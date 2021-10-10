from django import forms
from pagedown.widgets import PagedownWidget
from .models import Answer

class AnswerForm(forms.Form):
    content = forms.CharField(widget=PagedownWidget)