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
    path('signup/',views.signupview,name='signup'),
    path('dashboard/',views.DB_view ,name='Dashboard'),
    path('about/',views.aboutview ,name='about'),
    path('shop/',views.shopview ,name='shop'),
    path('checkout/',views.checkoutview ,name='checkout'),
    path('cart/',views.cartview ,name='cart'),
    path('pricing/',views.pricingview ,name='pricing'),
    path('confirmation/',views.confirmationview ,name='confirmation'),
    path('Product-single/',views.productDetailview ,name='Product_de'),
    path('shop-sidebar/',views.shopwithsidebarview ,name='shop-sidebar'),
    path('contact.html/',views.contactview ,name='contact'),
    path('404.html/',views.page_404view ,name='404'),
    path('coming-soon.html/',views.comingsoonview ,name='soon'),
    path('faq.html/',views.FQAview ,name='faq'),
    path('dashboard.html/',views.dashview ,name='dash'),
    path('order.html/',views.ordersview ,name='orders'),
    path('address.html/',views.addressview ,name='add'),
    path('profile-details.html',views.Profileview ,name='profile'),
    path('forget-password.html/',views.forget_passwordview ,name='forget'),
    path('blog-left-sidebar.html/',views.blog_lf_sidebarviews,name='blog-lf'),
    path('blog-right-sidebar.html/',views.blog_rg_sidebarviews,name='blog-rg'),
    path('blog-full-width.html/',views.blog_full_width_sidebarviews,name='blog-fw'),
    path('blog-gird.html/',views.blog_2_coloumeviews,name='blog-2'),
    path('blog-single.html/',views.blog_singleviews,name='blog-single'),
    path('typography.html/',views.typographyviews,name='typo'),
    path('buttons.html',views.btnviews,name='btn'),
    path('alerts.html',views.aletrsviews,name='alerts')

   

]
