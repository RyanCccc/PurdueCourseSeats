from django.shortcuts import render, redirect


def index(request):
    context = None
    return render(request, 'index_bootstrap.html', context)
