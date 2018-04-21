from django.http import HttpResponse

from mainapp.models import Offer, Question
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = 'mainapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Offer.objects.order_by('-id')


class HomeView(generic.ListView):
    model = Offer
    template_name = 'mainapp/home.html'


class BaseView(generic.ListView):
    model = Question
    template_name = 'mainapp/base.html'