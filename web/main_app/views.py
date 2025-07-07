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
def forget_passwordview(request):
    messages.info(request,"Your Password change successfully")
    return render(request,"forget-password.html")
def DB_view(request):
    return render(request,'dashboard.html')
def shopview(request):
    return render(request,'shop.html')
def checkoutview(request):
    return render(request,'checkout.html')
def cartview(request):
    return render(request,'cart.html')
def pricingview(request):
    return render(request,'pricing.html')
def confirmationview(request):
    return render(request,'confirmation.html')
def productDetailview(request):
    return render(request,'Product-single.html')
def shopwithsidebarview(request):
    return render(request,'shop-sidebar.html')
def contactview(request):
    return render(request,'contact.html')
def aboutview(request):
    return render(request,'about.html')
def page_404view(request):
    return render(request,'404.html')
def comingsoonview(request):
    return render(request,'coming-soon.html')
def FQAview(request):
    return render(request,'faq.html')
def dashview(request):
    return render(request,'dashboard.html')
def ordersview(request):
    return render(request,'order.html')
def addressview(request):
    return render(request,'address.html')
def Profileview(request):
    return render(request,'profile-details.html')
def blog_lf_sidebarviews(request):
    return render(request,'blog-left-sidebar.html')
def blog_rg_sidebarviews(request):
    return render(request,'blog-right-sidebar.html')
def blog_full_width_sidebarviews(request):
    return render(request,'blog-full-width.html')
def blog_2_coloumeviews(request):
    return render(request,'blog-grid.html')
def blog_singleviews(request):
    return render(request,'blog-single.html')
def typographyviews(request):
    return render(request,'typography.html')
def btnviews(request):
    return render(request,'buttons.html')
def aletrsviews(request):
    return render(request,'alerts.html')
