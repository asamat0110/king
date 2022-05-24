from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject_massage', 'massage']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'last_name'}),
            'email': forms.EmailField(attrs={'class': 'form-group', 'placeholder': 'email'}),
            'subject_massage': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'subject_massage'}),
            'massage': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'massage'}),
        }