from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm, SearchForm
from django.db.models import Q
from .forms import UserRegistrationFrom, UserAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# -----------------------------------REGISTER------------------------------
def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            data = form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = UserRegistrationFrom()
    return render(request, 'product/register.html', {'register_form': form})

# -----------------------------------LOGIN------------------------------
def loginUser(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('index')
    else:
        form = UserAuthenticationForm()
    return render(
        request,
        'product/login.html', {'login_form': form}
    )

# -----------------------------------LOGOUT------------------------------

def logoutUser(request):
    logout(request)
    return redirect('login')


# ---------------READ------------------------
def index(request):

    return render(
        request,
        'product/index.html'
    )

def about(request):
    return render(
        request,
        'product/about.html'
    )

def services(request):
    return render(
        request,
        'product/services.html'
    )

def work(request):
    return render(
        request,
        'product/work.html'
    )


# -----------------------------------CREATE------------------------------
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save()
            #data = Contact.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'from_for_temp': form,
    }
    return render(
        request,
        'product/contact.html', context
    )
