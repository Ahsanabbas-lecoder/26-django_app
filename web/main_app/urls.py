"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.indexview ,name='home'),
    path('login/',views.loginview ,name='login'),
    path('signin/',views.signupview,name='signin'),
    # path('dashboard/',views.signup ,name=' '),
    # path(' about/',views.signup ,name=' '),
    # path(' address/',views.signup ,name=' '),
    # path(' alrets/',views.signup ,name=' '),
    # path(' blog-full-width/',views.signup ,name=' '),
    # path(' blog-gird/',views.signup ,name=' '),
    # path(' blog-left-sidebar/',views.signup ,name=' '),
    # path(' blog-right-sidebar/',views.signup ,name=' '),
    # path(' blog-single/',views.signup ,name=' '),
    # path(' buttons/',views.signup ,name=' '),
    # path(' checkout/',views.signup ,name=' '),
    # path(' coming-out/',views.signup ,name=' '),
    # path(' comfirmation/',views.signup ,name=' '),
    # path(' contact/',views.signup ,name=' '),
    # path(' empty-cart/',views.signup ,name=' '),
    # path(' faq/',views.signup ,name=' '),
    # path(' forget-password/',views.signup ,name=' '),
    # path(' order/',views.signup ,name=' '),
    # # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),
    # path(' /',views.signup ,name=' '),

]
