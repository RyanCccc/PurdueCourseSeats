from django.shortcuts import render, redirect


def index(request):
    context = None
    return render(request, 'index_bootstrap.html', context)

def not_completed(request):
    context = None
    return render(request, 'notcompleted.html', context)
