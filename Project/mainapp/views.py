from django.http import HttpResponse

from mainapp.models import Offer
from django.views import generic

def index(request):
    return HttpResponse("it works")

class HomeView(generic.DetailView):
    model = Offer
    template_name = 'mainapp/home.html'


class BaseView(generic.DetailView):
    model = Offer
    template_name = 'mainapp/base.html'
