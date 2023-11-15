from django import forms
from .models import Storecollection

class StoreSelectionForm(forms.ModelForm):
    class Meta:
        model = Storecollection
        fields = ['storeid']
        #widgets = {'storeid': forms.CheckboxSelectMultiple}