from django.shortcuts import render
from django.contrib.auth import login,aauthenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .form import Usersignup

# Create your views here.
def indexview(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
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
def signup(request):
    if request.method == "POST":
        form = Usersignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'signup.html',{'form':form})
    return render(request,'signup.html')
