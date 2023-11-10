from django import forms
from .models import GroceryStore, UserStoreSelection

class StoreSelectionForm(forms.ModelForm):
    class Meta:
        model = UserStoreSelection
        fields = ['stores']
        widgets = {
            'stores': forms.CheckboxSelectMultiple
        }