from django.shortcuts import render
from .models import *

# CRUD


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
def contact(request):
    return render(
        request,
        'product/contact.html'
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
