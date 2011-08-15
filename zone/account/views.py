from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, CreateForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print "I get here"
            user = authenticate(username=User.objects.get(email=form.cleaned_data['email']).username, password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    print "no here"
    return render_to_response("account/login.html", {'form':form}, context_instance=RequestContext(request))

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CreateForm()
    return render_to_response("account/create.html", {"form":form}, context_instance=RequestContext(request))
    