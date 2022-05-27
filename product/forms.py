from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationFrom(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Search'}),)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject_massage', 'massage']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-group', 'placeholder': 'email'}),
            'subject_massage': forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'subject_massage'}),
            'massage': forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'massage'}),
        }