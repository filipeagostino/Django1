from django import forms

from .models import Contacts

class ItemForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ('name', 'phone', 'email', 'city')