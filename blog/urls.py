"""coding_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog.views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('services/', services),
    path('contact/', contact, name="contact"),
    path('signup/', handlesignup, name="signup"),
    path('login/', handlelogin, name="login"),
    path('logout/', handlelogout, name="logout"),
    path('<slug:slug>/index.htm', blogPost),
    # path('ask/', ask),
    path('<slug:cat>/<slug:slug>', blogPostDetails, name="answ"),
]
