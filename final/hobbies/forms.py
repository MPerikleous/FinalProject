from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
        }
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name[0].isupper():
            raise forms.ValidationError("First letter should be in capital!")
        return name