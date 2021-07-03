"""ideathon URL Configuration

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
from knowme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.firstpage, name="firstpage"),
    path('signup',views.signup, name="signup"),
    path('main1',views.main1, name="main1"),
    path('sub1',views.sub1, name="sub1"),
    path('sub11',views.sub11, name="sub11"),
    path('sub2',views.sub2, name="sub2"),
    path('sub21',views.sub21, name="sub21"),
    path('sub',views.sub3, name="sub3"),
]
