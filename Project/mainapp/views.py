from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html', {})

def base(request):
    return render(request, 'mainapp/base.html', {})

