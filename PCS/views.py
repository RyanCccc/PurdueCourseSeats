from django.shortcuts import render, redirect


def index(request):
    user = request.user
    if not user.is_authenticated():
        user = None
    context = dict(user=user)
    return render(request, 'index_bootstrap.html', context)

def not_completed(request):
    context = None
    return render(request, 'notcompleted.html', context)
