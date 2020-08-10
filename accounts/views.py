from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

# GET AND POST REQUESTS 
#POST : Sending information to server  :::: use it for submiting data ::::: (and it doesnt show ur details in address bar)
#GET : Retrieving info from server  :::: use it for fetching data :::::
def signup(request):
    if request.method == 'POST':
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.get(username=request.POST['username'])  # we used uname if theres some usr with same name
                return render(request, 'accounts/signup.html', {'error':'Username can\'t be same'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)    # creates user and logs it in
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST: 
                return redirect(request.POST['next'])
            return render(request, 'accounts/login.html', {'error':'Login Successful'})
        else: 
            return render(request, 'accounts/login.html', {'error':'Invalid Username and Password'})
    else:
        return render(request, 'accounts/login.html')

