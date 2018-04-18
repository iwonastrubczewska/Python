
from mainapp.models import Offer
from django.views import generic


class HomeView(generic.DetailView):
    model = Offer
    template_name = 'mainapp/home.html'


class BaseView(generic.DetailView):
    model = Offer
    template_name = 'mainapp/base.html'
