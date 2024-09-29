"""
URL configuration for diy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from diyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login),
    path('home',views.home),
    path('register', views.register),
    path('about', views.about),
    path('cpassword', views.cpassword),
    path('contact', views.contact),
    path('se', views.serviceengineers),
    path('tutorial', views.tutorial),
    path('payment', views.payment),
    path('user', views.user),
    path('adds', views.addservice),
    path('booking', views.booking),
    path('service', views.service),
    path('plums', views.splum),
    path('userreg', views.userreg),
    path('sreg', views.sreg),
    path('profile', views.profile),
    path('support', views.support),
    path('offer', views.offer),


]
