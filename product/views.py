from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

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