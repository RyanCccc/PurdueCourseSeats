from django.shortcuts import render, redirect

def guest_required(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('user_mode_dashboard')
        else:
            return func(request, *args, **kwargs)
    return wrap
