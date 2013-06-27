from django.shortcuts import render, redirect
from django.http import HttpResponse

from user_mode.models import User, authenticate
from PCS import settings
from seats_check.util import ParserException, convert_term_to_code
# Create your views here.

def index(request):
    username = request.COOKIES.get('username')
    if request.method == 'GET':
        if not username:
            return redirect('user_mode_login')
        else:
            user = User.objects.get(username = username)
            context = {
                'username' : username,
                'email' : user.email,
                'sections' :  user.sections.all()
            }
            return render(request, 'index.html', context)
    elif request.method == 'POST':
        if not username:
            return redirect('user_mode_login')
        else:
            param = request.POST
            crn = param.get('crn')
            term = param.get('term')
            if not term:
                term = settings.CURRENT_TERM 
            else:
                term = convert_term_to_code(term)
            user = User.objects.get(username = username)
            context = {
                'username' : username,
                'email' : user.email,
                'sections' :  user.sections.all(),
                'error' : '',
            }
            try:
                user.add_section(crn, term)
            except ParserException as e:
                context['error'] = e.message
                return render(request, 'index.html', context) 
            return render(request, 'index.html', context) 

def login(request):
    if request.method == 'GET':
        return render(request,'login.html', {'error':''})
    elif request.method == 'POST':
        param = request.POST
        username = param.get('username')
        password = param.get('password')
        email = param.get('email')
        user = authenticate(username, password)
        if not user: 
            return render(
                        request,'login.html', 
                        {'error':'Incorrect username or password'}
                    )
        else:
            respond = redirect('user_mode_index')
            respond.set_cookie('username', username)
            return respond
    else:
        return render(request,'login.html', {'error':''})

def logout(request):
    pass

def register(request):
    if request.method == 'GET':
        return render(request,'register.html', {'error':''})
    elif request.method == 'POST':
        param = request.POST
        username = param.get('username')
        password = param.get('password')
        email = param.get('email')
        if User.objects.filter(username = username).exists():
            return render(request,'register.html', {'error':'Username Exists'})
        else:
            user = User(
                username = username,
                password = password,
                email = email
            )
            user.save()
            respond = redirect('user_mode_index')
            respond.set_cookie('username', username)
            return respond
    else:
        return render(request,'register.html', {'error':''})
