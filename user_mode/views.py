from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from user_mode.models import MyUser
from PCS import settings
from seats_check.util import (
    ParserException,
    convert_term_to_code,
    convert_classname,
    get_all_secs_by_class
)
from seats_check.models import Section
from decorators import guest_required
from tasks import send_email

# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    if request.method == 'GET':
        my_user = MyUser.objects.get(user=user)
        context = {
            'username' : user.username,
            'email' : user.email,
            'sections' :  my_user.sections.all()
        }
        return render(request, 'dashboard.html', context)
    elif request.method == 'POST':
        my_user = MyUser.objects.get(user=user)
        param = request.POST
        crn = param.get('crn')
        term = param.get('term')
        if not term:
            term = settings.CURRENT_TERM
        else:
            term = convert_term_to_code(term)
        context = {
            'email' : user.email,
            'sections' :  my_user.sections.all(),
            'error' : '',
        }
        try:
            sec = my_user.add_section(crn, term)
            if sec:
                msg = "You successfully subscribe section:%s \n" % sec
                try:
                    send_email.delay([my_user.user.email,], msg)
                except ImportError as e: 
                    pass
                    #send_email([my_user.user.email,], msg)
        except ParserException as e:
            context['error'] = e.message
            return render(request, 'dashboard.html', context) 
        return render(request, 'dashboard.html', context)

@guest_required
def login(request):
    if request.method == 'GET':
        return render(request,'login.html', {'error':''})
    elif request.method == 'POST':
        param = request.POST
        username = param.get('username')
        password = param.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            _login(request, user)
            respond = redirect('user_mode_dashboard')
        else:
            return render(
                        request,'login.html', 
                        {'error':'Incorrect login'}
                    )
        return respond

@login_required
def logout(request):
    _logout(request)
    return redirect('home')

@guest_required
def register(request):
    if request.method == 'GET':
        return render(request,'register.html', {'error':''})
    elif request.method == 'POST':
        param = request.POST
        username = param.get('username')
        firstname = param.get('firstname')
        lastname= param.get('lastname')
        email = param.get('email')
        password = param.get('password')
        repassword = param.get('repassword')
        if not username or not firstname or not lastname: 
            return render(request,'register.html', {'error':'Please fill out all required fields'})
        if not email:
            return render(request,'register.html', {'error':'Please fill out address'})
        if repassword != password:
            return render(request,'register.html', {'error':'Password not same'})
        try:
            validate_email(email)
        except ValidationError:
            return render(request,'register.html', {'error':'Please use correct email'})
        if User.objects.filter(username = username).exists():
            return render(request,'register.html', {'error':'Username Exists'})
        elif User.objects.filter(email = email).exists():
            return render(request,'register.html', {'error':'Email Exists'})
        else:
            my_user = MyUser.objects.create_user(
                    username,
                    email,
                    password,
                    firstname,
                    lastname
                    )
            user = my_user.user
            user = authenticate(username=username, password=password)
            _login(request, user)
            respond = redirect('user_mode_dashboard')
            return respond
    else:
        return render(request,'register.html', {'error':''})

@login_required
def crn_search(request):
    if request.method == 'GET':
        context = None
    if request.method == 'POST':
        class_name = request.POST.get('classname')
        term = request.POST.get('term')
        if not term:
            term = settings.CURRENT_TERM 
        else:
            term = convert_term_to_code(term)
        if class_name:
            try:
                sub, cnbr = convert_classname(class_name)
                classes = get_all_secs_by_class(sub, cnbr, term)
            except ParserException as e:
                context = {'error': e.message}
                return render(request, 'crn_search.html', context)
            classes = sorted(classes, key = lambda cl: cl['class_time'].start_time)
            context = {
                'classes': classes,
                'error': ''
            }
        else:
            context = {'error': 'Please use right class name'}
    return render(request, 'crn_search.html', context)

@login_required
def remove_crn(request):
    crn = request.POST.get('crn')
    # TODO
    # Add term
    sec = Section.objects.get(crn=crn)
    user = request.user
    myuser = user.myuser
    myuser.sections.remove(sec)
    if not sec.myuser_set.count():
        Section.delete(sec)
    return redirect('user_mode_dashboard')

@login_required
def profile(request):
    user = request.user
    context = {
        'user' : user,
        'error' : '',
    }
    if request.method == 'GET':
        return render(request, 'profile.html', context)
    elif request.method == 'POST':
        param = request.POST
        firstname = param.get('firstname')
        lastname= param.get('lastname')
        email = param.get('email')
        if not firstname or not lastname: 
            context['error'] = 'Please fill out your name'
            return render(
                request,'profile.html', 
                context
            )
        if not email:
            context['error'] = 'Please fill out your email'
            return render(
                request,'profile.html', 
                context
            )
        try:
            validate_email(email)
        except ValidationError:
            context['error'] = 'Please use correct email'
            return render(
                request,'profile.html', 
                context
            )
        if User.objects.filter(email = email).exists() and user.email != email:
            context['error'] = 'Email exists'
            return render(
                request,'profile.html', 
                context
            )
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        print firstname, lastname, email
        user.save()
        return render(request, 'profile.html', context)
