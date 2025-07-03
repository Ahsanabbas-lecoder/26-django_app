from django.shortcuts import render,redirect
# from django.contrib.auth import login,aauthenticate,logout
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .form import Usersignupform
from django.contrib import messages

# Create your views here.
def indexview(request):
    return render(request,'index.html')

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

    # return render(request,'login.html')
def signupview(request):
    if request.method == "POST":
        form = Usersignupform(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            messages.success(request,f"Your account has been created")
            return redirect('login')
        else:
            messages.error(request,f"Your don't have permission")


    else:
            form = Usersignupform()
            return render(request,'signin.html',{'form':form})
    return render(request,'signin.html')

def logout_view(request):
    logout(request)
    messages.info(request,"you have successfully logged out")
    return redirect('login')