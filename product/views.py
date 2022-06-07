from django.shortcuts import render, redirect
from .models import Contact, Feedback, Project
from .forms import ContactForm, SearchForm
from django.db.models import Q
from .forms import UserRegistrationFrom, UserAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

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
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login')
                else:
                    return redirect('Disabled account')
            else:
                return redirect('Invalid login')
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
    feedback_temp = Feedback.objects.all()
    project_temp = Project.objects.all()
    context = {
        'feedback_tmp': feedback_temp,
        'project_tmp': project_temp
    }
    return render(
        request,
        'product/index.html', context
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
    work_temp = Project.objects.all()
    context = {
        'work_tmp': work_temp
    }
    return render(
        request,
        'product/work.html', context
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


# -----------------------------------SEARCH------------------------------
def search(request):
    search1 = request.GET.get('search')
    if search1:
        info = Project.objects.filter(Project_name=search1)
    else:
        info = Project.objects.filter(kinds=search1)
    return render(request, 'base.html', {'projects': info})