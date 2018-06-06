from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from mainapp.models import Offer, Question
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
from .forms import OfferForm, UserForm, NewUserForm


# strona glowna - mozna przejsc do dodawania ofetry lub przeglądania ofert
# lista pracodawcow
class IndexView(ListView):
    template_name = 'mainapp/index.html'
    model = Employer



# wyswietla liste ofert
class HomeView(ListView):
    model = Offer
    template_name = 'mainapp/home.html'



# wyswietla szczegoly oferty
class OfferView(DetailView):
    model = Offer
    template_name = 'mainapp/offer.html'

    def get_object(self):
        return get_object_or_404(Offer, pk=self.kwargs.get("pk"))


def NewOffer(request):
    form = OfferForm()
    return render(request, 'mainapp/newoffer.html', {'form': form})

def SignIn(request):
    form = NewUserForm()
    return render(request, 'mainapp/signin.html', {'form': form})

def LogIn(request):
    form = UserForm()
    return render(request, 'mainapp/login.html', {'form': form})


#to tylko zeby działało:
def Contact(request):
    form = UserForm()
    return render(request, 'mainapp/contact.html', {'form': form})





#class BaseView(ListView):
   #template_name = 'mainapp/base.html'

