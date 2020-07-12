from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'bolg/home.html')


def about(request):
    return render(request,'bolg/about.html')

    
def about2(request):
    return render(request,'bolg/about2.html')