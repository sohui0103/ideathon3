from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def firstpage(request):
    return render(request, 'firstpage.html')

def signup(request):
    return render(request, 'signup.html')

def main1(request):
    return render(request, 'main1.html')

def sub1(request):
    return render(request, 'sub1.html')

def sub11(request):
    return render(request, 'sub11.html')

def sub2(request):
    return render(request, 'sub2.html')

def sub21(request):
    return render(request, 'sub21.html')

def sub3(request):
    return render(request, 'sub3.html')

