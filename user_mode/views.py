from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as _login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from user_mode.models import MyUser
from PCS import settings
from seats_check.util import ParserException, convert_term_to_code
# Create your views here.

def index(request):
    user = request.user
    import pdb; pdb.set_trace()
    if request.method == 'GET':
        if not user.is_authenticated():
            return redirect('user_mode_login')
        else:
            my_user = MyUser.objects.get(user=user)
            context = {
                'username' : user.username,
                'email' : user.email,
                'sections' :  my_user.sections.all()
            }
            return render(request, 'index.html', context)
    elif request.method == 'POST':
        if not user.is_authenticated():
            return redirect('user_mode_login')
        else:
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
                my_user.add_section(crn, term)
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
        email = param.get('email')
        password = param.get('password')
        user = authenticate(username=username, password=password)
        #TODO catch correct exception
        if user is not None:
            _login(request, user)
            respond = redirect('user_mode_index')
        else:
            return render(
                        request,'login.html', 
                        {'error':'Incorrect login'}
                    )
        return respond

def logout(request):
    pass

def register(request):
    if request.method == 'GET':
        return render(request,'register.html', {'error':''})
    elif request.method == 'POST':
        param = request.POST
        username = param.get('username')
        email = param.get('email')
        password = param.get('password')
        if User.objects.filter(username = username).exists():
            return render(request,'register.html', {'error':'Username Exists'})
        else:
            my_user = MyUser.objects.create_user(username, email, password)
            user = my_user.user
            authenticate(username, password)
            _login(request, user)
            respond = redirect('user_mode_index')
            return respond
    else:
        return render(request,'rmy_egister.html', {'error':''})
