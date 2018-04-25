from django.http import HttpResponse
from django.shortcuts import render

from mainapp.models import Offer, Question
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = 'mainapp/index.html'
    context_object_name = 'latest_employers_list'

    def get_queryset(self):
        return Employer.objects.order_by('-id')

def Employers(request):
    employers = Employer.objects.all()
    return render(request, "employers.html", {"employers":employers})

class HomeView(generic.ListView):
    model = Offer
    template_name = 'mainapp/home.html'


class BaseView(generic.ListView):
    model = Question
    template_name = 'mainapp/base.html'