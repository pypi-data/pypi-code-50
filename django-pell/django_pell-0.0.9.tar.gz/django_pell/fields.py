from django import forms
from django_pell.widgets import PellWidget


class PellField(forms.CharField):
    """Form field which applies the PellWidget as a default."""

    widget = PellWidget()
