from django.shortcuts import render, redirect

def banned(request):
    context = None
    return render(request, 'banned.html', context)

def index(request):
    context = None
    return render(request, 'index_bootstrap.html', context)

def api(request):
    context = None
    return render(request, 'api.html', context)

def not_completed(request):
    context = None
    return render(request, 'notcompleted.html', context)

def contact(request):
    context = None
    return render(request, 'contact.html', context)
