from django.shortcuts import render
from numpy.core import generic
from mainapp.models import Offer
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class HomeView(generic.DetailView):
    model = Offer
    template_name = 'mainapp/home.html'


class BaseView(generic.DetailView):
    model = Offer
    template_name = 'mainapp/base.html'
